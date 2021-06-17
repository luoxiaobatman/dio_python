from ...delegate.abstract.memory_delegate import MemoryDelegate
from ...share.entity import Entity


class DelegateMemoryNoop(MemoryDelegate):
    async def _transform(self, option = None) -> Entity:
        return self._entity_
