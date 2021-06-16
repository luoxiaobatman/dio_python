from abc import abstractmethod
from copy import deepcopy
from typing import List, Optional, Tuple, TypeVar, Type, Generic
# from .core.option_base import OptionBase
from .core.source.source_base import SourceBase
from ..schemable.schemable_python.schemable_python import SchemablePython
from ..share.entity import Entity
from ..schemable.typing import Schema


IoDelegate = None


class _Base_:
    source: SourceBase
    schema: Schema
    def __init__(self, source, schema):
        self.source = source
        self.schema = schema


class OptionBase:
    _base_: _Base_
    def __init__(self, source, schema=None):
        assert source is not None
        self._base_ = _Base_(source, schema)


E = TypeVar('E', bound=Entity)
RO = TypeVar('RO', bound=OptionBase)
WO = TypeVar('WO', bound=OptionBase)
O = TypeVar('O', bound=OptionBase)


class IoDelegate(SchemablePython, Generic[E, RO, WO]):
    """
    TODO, draw ascii
    """
    _entity_: Optional[Entity]
    def __init__(self, entity=None) -> None:
        self._entity_ = entity
    
    Entity: Type[E] = None
    ReadOption: Type[RO] = None
    WriteOption: Type[WO] = None
    # TODO 感觉不是很好的办法
    forked: List[Tuple[Type[IoDelegate], RO, WO]] = None
    
    async def _transform(self, option: RO = None) -> Optional[E]:
        return self._entity_
    
    @abstractmethod
    async def _read(self, option: RO = None) -> Optional[E]:
        raise NotImplementedError
    
    @abstractmethod
    async def _write(self, option: WO = None) -> None:
        raise NotImplementedError
    
    async def flow(self, ro: RO = None, wo: WO = None) -> Optional[E]:
        if self._entity_:
            await self._write(wo)
        else:
            self._entity_ = await self._read(ro)
        result = []
        entity = await self._transform()
        result.append(entity)
        if self.__class__.forked:
            rr = []
            for Delegate, ro, wo in self.__class__.forked:
                rr.append(await Delegate(deepcopy(entity)).flow(ro, wo))
            result.append(rr)
        return result
    
    @classmethod
    def fork(clz, forked: List[Tuple[IoDelegate, RO, WO]]):
        if clz.forked:
            forked = clz.forked + forked
        
        ChainedDelegate = type("Chained", (clz,), {})
        ChainedDelegate.forked = forked
        return ChainedDelegate
    
    @classmethod
    def serial():
        # TODO
        raise NotImplementedError
