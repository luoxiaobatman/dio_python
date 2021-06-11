from typing import Generic, TypeVar


E = TypeVar('E')


class WithEntity(Generic[E]):
    """
    WHY
        mixin
        WriteOption的Entity定义命名强制为entity
    """
    entity: E
