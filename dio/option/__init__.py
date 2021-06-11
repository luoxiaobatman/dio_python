from typing import Tuple
from urllib3.util.retry import Retry

from dio import OptionHttp

from api_base.util.requests.constant import DEFAULT_CONNECT_TIMEOUT, DEFAULT_READ_TIMEOUT, NO_READ_RETRY


class _PoolClientHttp_:
    timeout: Tuple[float, float]
    retry: Retry
    
    def __init__(self, timeout, retry):
        self.timeout = timeout
        self.retry = retry


class PoolClientOptionHttp(OptionHttp):
    _pool_client_http_: _PoolClientHttp_
    def __init__(self, timeout: Tuple[float, float] = (DEFAULT_CONNECT_TIMEOUT, DEFAULT_READ_TIMEOUT), retry: Retry = NO_READ_RETRY, **kargs):
        super().__init__(**kargs)
        self._pool_client_http_ = _PoolClientHttp_(timeout, retry)
