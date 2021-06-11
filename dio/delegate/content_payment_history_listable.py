from typing import TypeVar, Optional

from dio import compile_schema

from api_base.g import G

from .abstract.pool_client_http_delegate import PoolClientHttpDelegate, PoolClientHttpRequest
from .content_payment_history import DelegateContentPaymentHistory
from ..entity import EntityContentPaymentHistoryListable
from ..source.oasis_service import io_source_oasis_service
from ..option import PoolClientOptionHttp


ReadOption = None
T = TypeVar('T', bound=ReadOption)


class ReadOption(PoolClientOptionHttp):
    with_summary: bool
    
    def __init__(self, path: str, with_summary: bool):
        super().__init__(path=path, source=io_source_oasis_service)
        self.with_summary = with_summary
        
    @staticmethod
    def summary():
        return ReadOption('/pictureDownload/total', with_summary=True)
    @staticmethod
    def next():
        return ReadOption('/pictureDownload/downloadHistory', with_summary=False)


class DelegateContentPaymentHistoryListable(EntityContentPaymentHistoryListable, PoolClientHttpDelegate[EntityContentPaymentHistoryListable, ReadOption, None]):
    def __init__(self,
                 uid: int,
                 sid: Optional[int] = None,
                 pid: Optional[int] = None,
                 cursor: Optional[str] = None,
                 count: Optional[int] = None) -> None:
        self.uid = uid
        self.sid = sid
        self.pid = pid
        self.cursor = cursor
        self.count = count
        
    ReadOption = ReadOption
    WriteOption = None
    Entity = EntityContentPaymentHistoryListable
    
    __schema__ = compile_schema({
        'list': ([('result', 'list')], [(None)], DelegateContentPaymentHistory),
        'next_cursor': (
            [('result', 'next_cursor')],
            [G.C.CURSOR_END],
        ),
        'summary': ('result', None, lambda x: x if 'list' not in x else None),
    })

    def _do_read(self, request: PoolClientHttpRequest, option: ReadOption) -> any:
        if option.with_summary:
            return request.get({'ouid': self.uid, 'sid': self.sid})
        else:
            return request.get({
                'ouid': self.uid,
                'sid': self.sid,
                'pid': self.pid,
                'cursor': self.cursor,
                'count': self.count,
            })
    def _post_read(self, entity: EntityContentPaymentHistoryListable, option: ReadOption) -> EntityContentPaymentHistoryListable:
        if option.with_summary:
            return entity
        entity.cursor = self.cursor
        entity.count = self.count
        return entity
