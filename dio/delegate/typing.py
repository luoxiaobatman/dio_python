from abc import abstractmethod
from typing import Optional, TypeVar, Type, Generic
from .core.option_base import OptionBase
from ..schemable.schemable_python.schemable_python import SchemablePython
from ..share.entity import Entity


E = TypeVar('E', bound=Entity)
RO = TypeVar('RO', bound=OptionBase)
WO = TypeVar('WO', bound=OptionBase)


class IoDelegate(SchemablePython, Entity, Generic[E, RO, WO]):
    # ---------------------------- 必然有的Helper START ----------------------------
    Entity: Type[E] = None
    ReadOption: Type[RO] = None
    WriteOption: Type[WO] = None
    # ---------------------------- 必然有的Helper START ----------------------------
    
    @abstractmethod
    def read(self, option: RO = None) -> Optional[E]:
        raise NotImplementedError
    
    @abstractmethod
    def write(self, option: WO = None) -> any:
        raise NotImplementedError
    
    def fill(self, option: RO = None) -> None:
        e = self.read(option)
        if e:
            for k, v in e.__dict__.items():
                setattr(self, k, v)
    
    # ----------------------------  ----------------------------
    """
    api_base项目使用的是gevent来做coroutine
    这里提供一个python3原生协程
    不要在api_base项目中使用!!!
    """
    async def async_read(self, option: RO = None) -> Optional[E]:
        raise NotImplementedError
    async def async_write(self, option: WO = None) -> any:
        raise NotImplementedError
