from abc import abstractmethod
from copy import deepcopy
from dio.delegate.abstract.memory_delegate import MemoryDelegate, OptionMemory
from dio.share.entity import Entity


class DelegateMemoryNoop(MemoryDelegate):
    async def _transform(self, option = None) -> Entity:
        return self._entity_
