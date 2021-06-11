from redis import Redis
from .option_base import OptionBase


class _Redis_:
    client: Redis
    
    def __init__(self, client):
        self.client = client


class OptionRedis(OptionBase):
    _redis_: _Redis_
    
    def __init__(self, client: Redis, *args, **kargs):
        super().__init__(*args, **kargs)
        self._redis_ = _Redis_(client)
