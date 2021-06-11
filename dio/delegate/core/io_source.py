from abc import abstractmethod
from typing import List, Type, Union
from ...schemable.typing import Schemable
from ...share.entity import Entity


class IoSource:
    """
    TLDR
        数据源
        数据源知道怎么解读自己返回的数据
    """
    host: str
    def __init__(self, host):
        self.host = host
    
    @abstractmethod
    def content(self, schemable_clz: Type[Schemable], unknown: any) -> Entity:
        raise NotImplementedError

    @abstractmethod
    def __repr__(self):
        raise NotImplementedError


class IoSourceRedis(IoSource):
    def content(self, schemable_clz: Type[Schemable], data: Union[str, List[str], None]) -> Entity:
        if isinstance(data, List):
            return schemable_clz.from_iterable_of_string(data)
        return schemable_clz.from_json(data)

    def __repr__(self):
        return 'IoSourceRedis instance'
    

class IoSourceStd(IoSource):
    def content(self, schemable_clz: Type[Schemable], data: str) -> Entity:
        return schemable_clz.from_json(data)

    def __repr__(self):
        return 'IoSourceStd instance'


class IoSourceLocalFile(IoSource):
    pass


class IoSourceWeibo(IoSource):
    pass
