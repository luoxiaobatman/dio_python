from logging import Logger
from ..registration import Registration


class Logging:
    @property
    def logger(self) -> Logger:
        return Registration.instance().logger
