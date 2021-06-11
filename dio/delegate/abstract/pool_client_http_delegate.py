from typing import TypeVar, Optional, Generic, Dict, Union

from dio import HttpDelegate, DelegateHttpRequest, Entity

from api_base.util.requests import PoolClientRequest, JsonOasisResponseCheckHooks

from ...source.oasis_service import IoSourceOasisService
from ...option import PoolClientOptionHttp


E = TypeVar('E', bound=Entity)
RO = TypeVar('RO', bound=PoolClientOptionHttp)
WO = TypeVar('WO', bound=PoolClientOptionHttp)


class PoolClientHttpRequest(DelegateHttpRequest):
    option: PoolClientOptionHttp
    
    @property
    def timeout(self):
        return self.option._pool_client_http_.timeout
    @property
    def retry(self):
        return self.option._pool_client_http_.retry
    
    def get(self, urlParams: Optional[Dict[str, str]]) -> any:
        # 再建一个对象 DelegateHttpRequestSouceOasis 来做请求???
        if isinstance(self.option._base_.source, IoSourceOasisService):
            return PoolClientRequest.get(
                self.url,
                headers=self.header,
                params=urlParams,
                hook=JsonOasisResponseCheckHooks(),
                timeout=self.timeout,
                retries=self.retry,
            )
        else:
            raise NotImplementedError

    def post(self, urlParams: Optional[Dict[str, str]], body: Optional[Union[str, dict]]):
        if isinstance(self.option._base_.source, IoSourceOasisService):
            return PoolClientRequest.post(
                self.url,
                params=urlParams,
                headers=self.header,
                data=body,
                hook=JsonOasisResponseCheckHooks(),
                timeout=self.timeout,
                retries=self.retry,
            )
        else:
            raise NotImplementedError


class PoolClientHttpDelegate(HttpDelegate[E, RO, WO], Generic[E, RO, WO]):
    def _build_request(self, option: PoolClientOptionHttp) -> PoolClientHttpRequest:
        return PoolClientHttpRequest(option)
