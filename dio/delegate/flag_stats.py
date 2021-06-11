
from typing import Dict, List

from dio import compile_schema, SchemablePython

from api_base.g import G
from api_base.entity.status_entity import Status
from api_base.util.json_util import to_json
from api_base.logger import logger

from .abstract.pool_client_http_delegate import PoolClientHttpDelegate, PoolClientHttpRequest
from ..constant import StatusTypeDef
from ..entity import FlagStats, FlagOption, EntityFlagStatsBatch
from ..constant import UserSettingKeyValueDef, UserSettingKey, UserSettingKeyDescriptor
from ..source.oasis_service import io_source_oasis_service
from ..option import PoolClientOptionHttp


ReadOption = None
WriteOption = None
KeyValueDef = UserSettingKeyValueDef
KeyDescriptor = UserSettingKeyDescriptor
Key = UserSettingKey


class ReadOption(PoolClientOptionHttp):
    cuid: int
    def __init__(self):
        super().__init__(source=io_source_oasis_service,
                         path='/flag-stats/read',
                         header={"Content-Type": "application/json;charset=UTF-8"})
    @staticmethod
    def cuid(cuid: int):
        read_option = ReadOption()
        read_option.cuid = cuid
        return read_option


class WriteOption(PoolClientOptionHttp):
    _v365: bool
    def __init__(self, _v365: bool):
        super().__init__(source=io_source_oasis_service,
                         path='/flag-stats/write',
                         header={"Content-Type": "application/json;charset=UTF-8"})
        self._v365 = _v365
    
    @staticmethod
    def v365() -> WriteOption:
        return WriteOption(True)
    

class DelegateFlagOption(FlagOption, SchemablePython):
    __schema__ = compile_schema({
        'option': 'option',
        'ouid': 'ouid',
        'sid': 'sid',
        'option': 'option',
        'count': 'count',
        'delta': ('delta', 0),
        'label': 'label',
    })


class DelegateFlagStats(FlagStats, PoolClientHttpDelegate[FlagStats, ReadOption, WriteOption]):
    def __init__(self, uid, sid, options: List[FlagOption] = []) -> None:
        self.uid = uid
        self.sid = sid
        self.options = options

    WriteOption = WriteOption
    Entity = FlagStats
    
    __schema__ = compile_schema({
        'uid': 'uid',
        'sid': 'sid',
        'options': ('options', None, DelegateFlagOption)
    })

    def _do_write(self, request: PoolClientHttpRequest, wo: WriteOption) -> None:
        logger.info('DelegateFlagStats write, %s', self)
        if wo._v365:
            good = FlagOption()
            bad = FlagOption()
            good.label = '看好'
            good.option = 0
            good.ouid = self.uid
            good.sid = self.sid
            good.count = 0
            bad.label = '不看好'
            bad.option = 1
            bad.ouid = self.uid
            bad.sid = self.sid
            bad.count = 0
            self.options = [good, bad]
        json_serialized = to_json(self)
        request.post(None, json_serialized)


class DelegateFlagStatsBatch(EntityFlagStatsBatch, PoolClientHttpDelegate[EntityFlagStatsBatch, ReadOption, WriteOption]):
    def __init__(self, batch: List[FlagStats]) -> None:
        self.batch = batch
    
    __schema__ = compile_schema({
        'batch': ('object', None, DelegateFlagStats),
    })
    
    ReadOption = ReadOption
    Entity = EntityFlagStatsBatch
    
    def _do_read(self, request: PoolClientHttpRequest, option: ReadOption):
        json_serialized = to_json(self.batch)
        return request.post({'cuid': option.cuid}, json_serialized)
    
    @staticmethod
    def fill_statues_flag(cuid: int, statuses: List[Status]):
        flag_statuses: List[Status] = [status for status in statuses if G.S.get(status.extra, ['moment', 'type'], None) == StatusTypeDef.type_image_subtype_flag.value]
        if flag_statuses:
            statss = []
            sid_map: Dict[int, Status] = {}
            for s in flag_statuses:
                sid_map[s.id] = s
                stats = DelegateFlagStats.Entity()
                stats.sid = s.id
                stats.uid = s.uid
                statss.append(stats)
            wrap = DelegateFlagStatsBatch(statss).read(DelegateFlagStatsBatch.ReadOption.cuid(cuid))
            for stat in wrap.batch:
                sid_map[stat.sid].flag = stat
