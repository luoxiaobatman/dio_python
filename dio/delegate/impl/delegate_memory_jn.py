from abc import abstractmethod
from copy import deepcopy
import asyncio
from ...delegate.typing import IoDelegate
from ...delegate.abstract.memory_delegate import MemoryDelegate, OptionMemory


class CoordinatedDelegate(IoDelegate):
    """
    jn concurrency的执行单元
    """
    async def flow(self, ro, wo, q: asyncio.Queue):
        r = []
        try:
            while 1:
                q.get_nowait()
                if self._entity_:
                    r.append(await self._write(wo))
                else:
                    r.append(await self._read(ro))
        except asyncio.QueueEmpty:
            return r


class DelegateMemoryJN(MemoryDelegate):
    """
    jn concurrency的头
    """
    async def _transform(self, option = None):
        raise self._entity_
    
    async def flow(self, ro, wo, q: asyncio.Queue):
        return await super().flow(ro, wo, q)
