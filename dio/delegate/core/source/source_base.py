from abc import abstractmethod
from typing import Type
from ....schemable.typing import Schemable, Schema
from ....share.entity import Entity


class SourceBase:
    host: str
    def __init__(self, host):
        self.host = host
    
    @abstractmethod
    def content(self, schemable_clz: Type[Schemable], unknown: any, schema: Schema = None) -> Entity:
        raise NotImplementedError

    @abstractmethod
    def __repr__(self):
        raise NotImplementedError
