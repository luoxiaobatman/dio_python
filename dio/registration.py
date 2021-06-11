from .mixin.immutable import Immutable
from logging import Logger


_instance_ = None

Registration = None


class Registration(Immutable):
    @property
    def logger(self) -> Logger:
        return tuple.__getitem__(self, 0)
    
    @staticmethod
    def instance() -> Registration:
        return _instance_
    
    @staticmethod
    def register(logger: Logger) -> None:
        global _instance_
        if _instance_ is None:
            _instance_ = Registration(logger)
