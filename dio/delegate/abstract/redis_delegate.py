from abc import abstractmethod
from redis import Redis
from typing import Optional, TypeVar, Type, Generic
from ..core.io_read_sink import IoReadSink
from ..core.option_redis import OptionRedis
from ..typing import IoDelegate
from ...share.entity import Entity


T = TypeVar('T', bound=IoDelegate)
E = TypeVar('E', bound=Entity)
RO = TypeVar('RO', bound=OptionRedis)
WO = TypeVar('WO', bound=OptionRedis)


# class HttpDelegate(IoDelegate[E, RO, WO], Generic[E, RO, WO]):

class RedisDelegate(IoDelegate[E, RO, WO], Generic[E, RO, WO]):
    Entity: Type[E] = None
    ReadOption: Type[RO] = None
    WriteOption: Type[WO] = None
    
    @abstractmethod
    def _do_read(self: T, client: Redis, option: RO) -> any:
        raise NotImplementedError
    @abstractmethod
    def _do_write(self: T, client: Redis, option: WO) -> any:
        raise NotImplementedError
    @abstractmethod
    def _do_invalidate(self: T, client: Redis, option: WO) -> any:
        raise NotImplementedError
    
    def _pre_read(self, option: RO = None) -> Optional[E]:
        return None
    def read(self, option: RO) -> Optional[E]:
        r = self._pre_read(option)
        if r:
            return r
        result = self._do_read(option._redis_.client, option)
        if isinstance(result, Entity):
            return result
        sink = IoReadSink(self.__class__, option._base_.source, result)
        # 父类允许子类其他骚操作
        return self._post_read(sink.content, option)
    def _post_read(self: T, entity: E, option: RO) -> E:
        return entity
        
    def write(self, option: WO):
        self._do_write(option._redis_.client, option)
    def delete(self, option: WO):
        self._do_invalidate(option._redis_.client)
