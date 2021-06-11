from dio.schemable.schemable_python.schemable_python import SchemablePython
from typing import List

from dio import compile_schema

from api_base.util.json_util import to_json

from .abstract.pool_client_http_delegate import PoolClientHttpDelegate, PoolClientHttpRequest
from ..entity import FlagUserInteract, FlagOption
from ..constant import UserSettingKeyValueDef, UserSettingKey, UserSettingKeyDescriptor
from ..source.oasis_service import io_source_oasis_service
from ..option import PoolClientOptionHttp


WriteOption = None
KeyValueDef = UserSettingKeyValueDef
KeyDescriptor = UserSettingKeyDescriptor
Key = UserSettingKey


class WriteOption(PoolClientOptionHttp):
    def __init__(self):
        super().__init__(source=io_source_oasis_service,
                         path='/flag-user-interact/write',
                         header={"Content-Type": "application/json;charset=UTF-8"})


class DelegateFlagUserInteract(FlagUserInteract, PoolClientHttpDelegate[FlagUserInteract, None, WriteOption]):
    def __init__(self, uid, options: List[FlagOption]) -> None:
        self.uid = uid
        self.options = options
    def write(self, option=WriteOption()) -> any:
        return super().write(option=option)
    
    WriteOption = WriteOption
    Entity = FlagUserInteract

    def _do_write(self, request: PoolClientHttpRequest, *args, **kargs) -> None:
        json_serialized = to_json(self)
        request.post(None, json_serialized)
