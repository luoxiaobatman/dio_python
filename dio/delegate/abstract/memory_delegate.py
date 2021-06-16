from abc import abstractmethod
from copy import deepcopy
from typing import List, Optional, Tuple, TypeVar, Type, Generic
from ..typing import IoDelegate, OptionBase
from ...share.entity import Entity

# from .core.option_base import OptionBase
# from ..schemable.schemable_python.schemable_python import SchemablePython


class OptionMemory(OptionBase):
    def __init__(self):
        super().__init__('mem://')
    

E = TypeVar('E', bound=Entity)
RO = TypeVar('RO', bound=OptionMemory)
WO = TypeVar('WO', bound=OptionMemory)
O = TypeVar('O', bound=OptionMemory)


class MemoryDelegate(IoDelegate[E, RO, WO], Generic[E, RO, WO]):
    @abstractmethod
    async def _transform(self, option: RO = None) -> Optional[E]:
        raise NotImplementedError
    
    async def _read(self, option: RO = None) -> Optional[E]:
        raise NotImplementedError
    
    async def _write(self, option: WO = None) -> None:
        pass
