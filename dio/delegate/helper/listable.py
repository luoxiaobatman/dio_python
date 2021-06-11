from typing import TypeVar, Generic, List
from ...share import Entity


T = TypeVar('T', bound=Entity)


class Listable(Generic[T]):
    """
    WHY
        mixin
        entity listable 命名统一
    Problem
        subclass.__annotations__ 找不到这里定义, TODOlx
    """
    list: List[T]
    next_cursor: str
