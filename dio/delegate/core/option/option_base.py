from ..source.source_base import SourceBase
from ....schemable.typing import Schema
from ....share.entity import Entity


class _Base_:
    source: SourceBase
    schema: Schema
    entity: Entity
    def __init__(self, source, schema, entity):
        self.source = source
        self.schema = schema
        self.entity = entity


class OptionBase:
    _base_: _Base_
    def __init__(self, source, schema=None, entity=None):
        assert source is not None
        self._base_ = _Base_(source, schema, entity)
