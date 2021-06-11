from ...mixin.immutable import Immutable


class _Next_(Immutable):
    @property
    def cursor(self) -> str:
        return tuple.__getitem__(self, 0)
    @property
    def count(self) -> int:
        return tuple.__getitem__(self, 1)
    def __init__(self, cursor, count):
        pass


class Nextable:
    """
    WHY
        ReadOption 的 mixin
        统一命名
    """
    _Next_ = _Next_
    _next_: _Next_
