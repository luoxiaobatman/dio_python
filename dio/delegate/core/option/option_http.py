from abc import abstractmethod
from typing import Dict, Generic, Optional, Type, TypeVar, Union

from ...typing import OptionBase


class _Http_:
    path: str
    header: Optional[Dict[str, str]]  # TODO HttpHeader
    def __init__(self, path: str, header=None):
        self.path = path
        self.header = header
    

class OptionHttp(OptionBase):
    _http_: _Http_
    def __init__(self, path: str, header=None, **kargs):
        super().__init__(**kargs)
        self._http_ = _Http_(path, header)



# class HttpHeaderDescriptor(Immutable):
#     token: str
#     rtc: str
#     values: List


# class HttpHeader:
#     # https://tools.ietf.org/html/rfc7231#section-5.3.2
#     ACCEPT = 'Accept'
    
#     # https://tools.ietf.org/html/rfc7231#section-5.3.3
#     ACCEPT_CHARSET = 'Accept-Charset'
    
#     # https://tools.ietf.org/html/rfc7231#section-5.3.4
#     ACCEPT_ENCODING = 'Accept-Encoding'
    
#     # https://tools.ietf.org/html/rfc7231#section-5.3.5
#     ACCEPT_LANGUAGE = 'Accept-Language'
    
#     # https://tools.ietf.org/html/rfc7233#section-2.3
#     ACCEPT_RANGES = 'Accept-Ranges'
    
#     # https://www.w3.org/TR/cors/
#     ACCESS_CONTROL_ALLOW_CREDENTIALS = 'Access-Control-Allow-Credentials'
    
#     # https://www.w3.org/TR/cors/
#     ACCESS_CONTROL_ALLOW_HEADERS = 'Access-Control-Allow-Headers'
    
#     # https://www.w3.org/TR/cors/
#     ACCESS_CONTROL_ALLOW_METHODS = 'Access-Control-Allow-Methods'
    
#     # https://www.w3.org/TR/cors/
#     ACCESS_CONTROL_ALLOW_ORIGIN = 'Access-Control-Allow-Origin'
    
#     # https://www.w3.org/TR/cors/
#     ACCESS_CONTROL_EXPOSE_HEADERS = 'Access-Control-Expose-Headers'
    
#     # https://www.w3.org/TR/cors/
#     ACCESS_CONTROL_MAX_AGE = 'Access-Control-Max-Age'
    
#     # https://www.w3.org/TR/cors/
#     ACCESS_CONTROL_REQUEST_HEADERS = 'Access-Control-Request-Headers'
    
#     # https://www.w3.org/TR/cors/
#     ACCESS_CONTROL_REQUEST_METHOD = 'Access-Control-Request-Method'
    
#     # https://tools.ietf.org/html/rfc7234#section-5.1
#     AGE = 'Age'
    
#     # https://tools.ietf.org/html/rfc7231#section-7.4.1
#     ALLOW = 'Allow'
    
#     # https://tools.ietf.org/html/rfc7235#section-4.2
#     AUTHORIZATION = 'Authorization'
    
#     # https://tools.ietf.org/html/rfc7234#section-5.2
#     CACHE_CONTROL = 'Cache-Control'
    
#     # https://tools.ietf.org/html/rfc7230#section-6.1
#     CONNECTION = 'Connection'
    
#     # https://tools.ietf.org/html/rfc7231#section-3.1.2.2
#     CONTENT_ENCODING = 'Content-Encoding'
    
#     # https://tools.ietf.org/html/rfc6266
#     CONTENT_DISPOSITION = 'Content-Disposition'
    
#     # https://tools.ietf.org/html/rfc7231#section-3.1.3.2
#     CONTENT_LANGUAGE = 'Content-Language'
    
#     # https://tools.ietf.org/html/rfc7230#section-3.3.2
#     CONTENT_LENGTH = 'Content-Length'
    
#     # https://tools.ietf.org/html/rfc7231#section-3.1.4.2
#     CONTENT_LOCATION = 'Content-Location'
    
#     # https://tools.ietf.org/html/rfc7233#section-4.2
#     CONTENT_RANGE = 'Content-Range'
    
#     # https://tools.ietf.org/html/rfc7231#section-3.1.1.5
#     CONTENT_TYPE = 'Content-Type'
    
#     # https://tools.ietf.org/html/rfc2109#section-4.3.4
#     COOKIE = 'Cookie'
    
#     # https://tools.ietf.org/html/rfc7231#section-7.1.1.2
#     DATE = 'Date'
    
#     # https://tools.ietf.org/html/rfc7232#section-2.3
#     ETAG = 'ETag'
    
#     # https://tools.ietf.org/html/rfc7231#section-5.1.1
#     EXPECT = 'Expect'
    
#     # https://tools.ietf.org/html/rfc7234#section-5.3
#     EXPIRES = 'Expires'
    
#     # https://tools.ietf.org/html/rfc7231#section-5.5.1
#     FROM = 'From'
    
#     # https://tools.ietf.org/html/rfc7230#section-5.4
#     HOST = 'Host'
    
#     # https://tools.ietf.org/html/rfc7232#section-3.1
#     IF_MATCH = 'If-Match'
    
#     # https://tools.ietf.org/html/rfc7232#section-3.3
#     IF_MODIFIED_SINCE = 'If-Modified-Since'
    
#     # https://tools.ietf.org/html/rfc7232#section-3.2
#     IF_NONE_MATCH = 'If-None-Match'
    
#     # https://tools.ietf.org/html/rfc7233#section-3.2
#     IF_RANGE = 'If-Range'
    
#     # https://tools.ietf.org/html/rfc7232#section-3.4
#     IF_UNMODIFIED_SINCE = 'If-Unmodified-Since'
    
#     # https://tools.ietf.org/html/rfc7232#section-2.2
#     LAST_MODIFIED = 'Last-Modified'
    
#     # https://tools.ietf.org/html/rfc5988
#     LINK = 'Link'
    
#     # https://tools.ietf.org/html/rfc7231#section-7.1.2
#     LOCATION = 'Location'
    
#     # https://tools.ietf.org/html/rfc7231#section-5.1.2
#     MAX_FORWARDS = 'Max-Forwards'
    
#     # https://tools.ietf.org/html/rfc6454
#     ORIGIN = 'Origin'
    
#     # https://tools.ietf.org/html/rfc7234#section-5.4
#     PRAGMA = 'Pragma'
    
#     # https://tools.ietf.org/html/rfc7235#section-4.3
#     PROXY_AUTHENTICATE = 'Proxy-Authenticate'
    
#     # https://tools.ietf.org/html/rfc7235#section-4.4
#     PROXY_AUTHORIZATION = 'Proxy-Authorization'
    
#     # https://tools.ietf.org/html/rfc7233#section-3.1
#     RANGE = 'Range'
    
#     # https://tools.ietf.org/html/rfc7231#section-5.5.2
#     REFERER = 'Referer'
    
#     # https://tools.ietf.org/html/rfc7231#section-7.1.3
#     RETRY_AFTER = 'Retry-After'
    
#     # https://tools.ietf.org/html/rfc7231#section-7.4.2
#     SERVER = 'Server'
    
#     # https://tools.ietf.org/html/rfc2109#section-4.2.2
#     SET_COOKIE = 'Set-Cookie'
    
#     # https://tools.ietf.org/html/rfc2965
#     SET_COOKIE2 = 'Set-Cookie2'
    
#     # https://tools.ietf.org/html/rfc7230#section-4.3
#     TE = 'TE'
    
#     # https://tools.ietf.org/html/rfc7230#section-4.4
#     TRAILER = 'Trailer'
    
#     # https://tools.ietf.org/html/rfc7230#section-3.3.1
#     TRANSFER_ENCODING = 'Transfer-Encoding'
    
#     # https://tools.ietf.org/html/rfc7230#section-6.7
#     UPGRADE = 'Upgrade'
    
#     # https://tools.ietf.org/html/rfc7231#section-5.5.3
#     USER_AGENT = 'User-Agent'
    
#     # https://tools.ietf.org/html/rfc7231#section-7.1.4
#     VARY = 'Vary'
    
#     # https://tools.ietf.org/html/rfc7230#section-5.7.1
#     VIA = 'Via'
    
#     # https://tools.ietf.org/html/rfc7234#section-5.5
#     WARNING = 'Warning'
    
#     # https://tools.ietf.org/html/rfc7235#section-4.1
#     WWW_AUTHENTICATE = 'WWW-Authenticate'