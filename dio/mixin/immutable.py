from abc import abstractmethod
from typing import TypeVar, Generic


T = TypeVar('T')


class Immutable(Generic[T], tuple):
    """
    TLDR:
        No Setter
    Usage:
        class ImmutableSubtype(Immutable[AnyType], AnyType):
            @property
            def foo(self):
                return tuple.__getitem__(self, 0|1|2|3...)
            def unfrozen(self):
                instance = AnyType()
                # ...
                return instance
        class ImmutableSubtype(Immutable):
            @property
            def foo(self):
                return tuple.__getitem__(self, 0|1|2|3...)
    """
    __slots__ = []

    def __new__(self, *args):
        return tuple.__new__(self, args)

    @abstractmethod
    def unfrozon(self) -> T:
        raise NotImplementedError
    
    # ---------------------------- 禁 ----------------------------
    def __getitem__(self, *args, **kargs):
        raise TypeError

    def __setitem__(self, *args, **kargs):
        raise TypeError

    def __setattr__(self, *args, **kargs):
        raise TypeError
