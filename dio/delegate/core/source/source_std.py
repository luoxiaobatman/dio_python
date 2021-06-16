from typing import Type
from ....schemable.typing import Schemable, Schema
from ....share.entity import Entity
from .source_base import SourceBase

class SourceStd(SourceBase):
    def content(self, schemable_clz: Type[Schemable], data: str, schema: Schema = None) -> Entity:
        return schemable_clz.from_json(data, schema)

    def __repr__(self):
        return 'SourceStd instance'
