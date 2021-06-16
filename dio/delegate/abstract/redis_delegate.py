# from abc import abstractmethod
# from redis import Redis
# from typing import Optional, TypeVar, Type, Generic, Union
# from ..core.io_read_sink import IoReadSink
# from ..core.option_redis import OptionRedis
# from ..typing import IoDelegate
# from ...share.entity import Entity


# T = TypeVar('T', bound=IoDelegate)
# E = TypeVar('E', bound=Entity)
# RO = TypeVar('RO', bound=OptionRedis)
# WO = TypeVar('WO', bound=OptionRedis)


# class RedisDelegate(IoDelegate[E, RO, WO], Generic[E, RO, WO]):
#     Entity: Type[E] = None
#     ReadOption: Type[RO] = None
#     WriteOption: Type[WO] = None
    
#     @abstractmethod
#     def _build_client(self, option: Union[RO, WO]):
#         raise NotImplementedError
#     @abstractmethod
#     async def _read(self: T, client: Redis, option: RO) -> any:
#         raise NotImplementedError
#     @abstractmethod
#     async def _write(self: T, client: Redis, option: WO) -> any:
#         raise NotImplementedError
    
#     async def read(self, option: RO) -> Optional[E]:
#         client = self._build_client()
#         result = await self._read(client, option)
#         if isinstance(result, Entity):
#             return result
#         sink = IoReadSink(self.__class__, option._base_.source, result)
#         return sink.content
#     async def write(self, option: WO):
#         return await self._write(option._redis_.client, option)
