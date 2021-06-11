from typing import Optional
from .io_source import IoSource
from ...share.entity import Entity


OptionBase = None
ImmutableOptionBase = None


cache = {}


class _Base_:
    source: IoSource
    entity: Optional[Entity]
    def __init__(self, source, entity):
        self.source = source
        self.entity = entity


class OptionBase:
    """
    option=命令
    """
    _base_: _Base_
    
    def __init__(self, source, entity=None):
        assert source is not None
        self._base_ = _Base_(source, entity)


class OptionMixinCacheable:
    """
    命令的结果可本地缓存
    """
