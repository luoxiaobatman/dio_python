from typing import Optional, TypeVar, Union
import json

from dio import compile_schema

from api_base.g import G

from .abstract.pool_client_http_delegate import PoolClientHttpDelegate, PoolClientHttpRequest
from ..constant.user_setting_key import UserSettingKeyValueDef
from ..entity import EntityContentPaymentHistory
from ..source.oasis_service import io_source_oasis_service
from ..option import PoolClientOptionHttp


T = TypeVar('T')


class ReadOption(PoolClientOptionHttp):
    def __init__(self):
        super().__init__(path='/pictureDownload/isPayed', source=io_source_oasis_service)


class WriteOption(PoolClientOptionHttp):
    def __init__(self):
        super().__init__(path='/pictureDownload/doDownload',
                         source=io_source_oasis_service,
                         header={"Content-Type": "application/json;charset=UTF-8"})


class DelegateContentPaymentHistory(EntityContentPaymentHistory, PoolClientHttpDelegate[EntityContentPaymentHistory, ReadOption, WriteOption]):
    def __init__(self,
                 cuid: int,
                 ouid: int,
                 sid: int,
                 pid: str,
                 cost: Optional[int] = None,
                 order_id: Union[str, None] = None) -> None:
        self.cuid = cuid
        self.sid = sid
        self.pid = pid
        self.ouid = ouid
        self.order_id = order_id
        self.cost = cost
    
    ReadOption = ReadOption
    WriteOption = WriteOption
    Entity = EntityContentPaymentHistory
    
    __schema__ = compile_schema({
        'cuid': 'cuid',
        'ouid': 'ouid',
        'sid': 'sid',
        'pid': 'pid',
    })
    
    def read(self: T, option=ReadOption()) -> Optional[EntityContentPaymentHistory]:
        return super().read(option=option)
    def write(self: T, option=WriteOption()) -> None:
        return super().write(option=option)

    def _do_read(self, request: PoolClientHttpRequest, option: ReadOption) -> any:
        # TODOlx, 重写设计接口, 返回更多信息
        r = request.get({'cuid': self.cuid, 'pid': self.pid})
        is_payed = G.S.get(r, 'result', False)
        if not is_payed:
            return None
        e = EntityContentPaymentHistory()
        e.cuid = self.cuid
        e.ouid = self.ouid
        e.sid = self.sid
        e.pid = self.pid
        e.cost = UserSettingKeyValueDef.cost_masked.value
        return e

    def _do_write(self, request: PoolClientHttpRequest, option: WriteOption) -> None:
        data = json.dumps({
            'cuid': self.cuid,
            'ouid': self.ouid,
            'sid': self.sid,
            'pid': self.pid,
            'cost': self.cost,
            'order_id': self.order_id,
        })
        request.post(None, data)
