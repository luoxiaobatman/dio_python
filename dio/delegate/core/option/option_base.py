from ..source.source_base import SourceBase
from ....schemable.typing import Schema


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