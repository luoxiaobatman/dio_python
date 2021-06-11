from abc import abstractmethod
from typing import TypeVar, Optional, Type, Generic, Dict, Union
from ..core.io_read_sink import IoReadSink
from ..core.option_http import OptionHttp
from ..typing import IoDelegate
from ...mixin.immutable import Immutable
from ...share.entity import Entity


T = TypeVar('T', bound=IoDelegate)
E = TypeVar('E', bound=Entity)
RO = TypeVar('RO', bound=OptionHttp)
WO = TypeVar('WO', bound=OptionHttp)
O = TypeVar('O', bound=OptionHttp)


class HttpStatusDescriptor(Immutable):
    @property
    def code(self):
        tuple.__getitem__(self, 0)
    @property
    def text(self):
        tuple.__getitem__(self, 1)
    @property
    def rfc(self):
        tuple.__getitem__(self, 2)


class HttpStatus:
    """
    TODOlx
    """
    # # 1xx Informational
    # CONTINUE = HttpStatusDescriptor(100, 'Continue', 'https://tools.ietf.org/html/rfc7231#section-6.2.1'),
    # SWITCHING_PROTOCOLS = HttpStatusDescriptor(101, "Switching Protocols", 'https://tools.ietf.org/html/rfc7231#section-6.2.2'),
    # # https://tools.ietf.org/html/rfc2518#section-10.1">WebDAV</a>
    # PROCESSING(102, "Processing"),
    # # https://code.google.com/p/gears/wiki/ResumableHttpRequestsProposal">A proposal for supporting
    # CHECKPOINT(103, "Checkpoint"),

    # # 2xx Success
    # # https://tools.ietf.org/html/rfc7231#section-6.3.1">HTTP/1.1: Semantics and Content, section 6.3.1</a>
    # OK(200, "OK"),
    # # https://tools.ietf.org/html/rfc7231#section-6.3.2">HTTP/1.1: Semantics and Content, section 6.3.2</a>
    # CREATED(201, "Created"),
    # # https://tools.ietf.org/html/rfc7231#section-6.3.3">HTTP/1.1: Semantics and Content, section 6.3.3</a>
    # ACCEPTED(202, "Accepted"),
    # # https://tools.ietf.org/html/rfc7231#section-6.3.4">HTTP/1.1: Semantics and Content, section 6.3.4</a>
    # NON_AUTHORITATIVE_INFORMATION(203, "Non-Authoritative Information"),
    # # https://tools.ietf.org/html/rfc7231#section-6.3.5">HTTP/1.1: Semantics and Content, section 6.3.5</a>
    # NO_CONTENT(204, "No Content"),
    # # https://tools.ietf.org/html/rfc7231#section-6.3.6">HTTP/1.1: Semantics and Content, section 6.3.6</a>
    # RESET_CONTENT(205, "Reset Content"),
    # # https://tools.ietf.org/html/rfc7233#section-4.1">HTTP/1.1: Range Requests, section 4.1</a>
    # PARTIAL_CONTENT(206, "Partial Content"),
    # # https://tools.ietf.org/html/rfc4918#section-13">WebDAV</a>
    # MULTI_STATUS(207, "Multi-Status"),
    # # https://tools.ietf.org/html/rfc5842#section-7.1">WebDAV Binding Extensions</a>
    # ALREADY_REPORTED(208, "Already Reported"),
    # # https://tools.ietf.org/html/rfc3229#section-10.4.1">Delta encoding in HTTP</a>
    # IM_USED(226, "IM Used"),

    # # 3xx Redirection
    # # https://tools.ietf.org/html/rfc7231#section-6.4.1">HTTP/1.1: Semantics and Content, section 6.4.1</a>
    # MULTIPLE_CHOICES(300, "Multiple Choices"),
    # # https://tools.ietf.org/html/rfc7231#section-6.4.2">HTTP/1.1: Semantics and Content, section 6.4.2</a>
    # MOVED_PERMANENTLY(301, "Moved Permanently"),
    # # https://tools.ietf.org/html/rfc7231#section-6.4.3">HTTP/1.1: Semantics and Content, section 6.4.3</a>
    # FOUND(302, "Found"),
    # # https://tools.ietf.org/html/rfc1945#section-9.3">HTTP/1.0, section 9.3</a>
    # @Deprecated
    # MOVED_TEMPORARILY(302, "Moved Temporarily"),
    # # https://tools.ietf.org/html/rfc7231#section-6.4.4">HTTP/1.1: Semantics and Content, section 6.4.4</a>
    # SEE_OTHER(303, "See Other"),
    # # https://tools.ietf.org/html/rfc7232#section-4.1">HTTP/1.1: Conditional Requests, section 4.1</a>
    # NOT_MODIFIED(304, "Not Modified"),
    # # https://tools.ietf.org/html/rfc7231#section-6.4.5">HTTP/1.1: Semantics and Content, section 6.4.5</a>
    #     */
    # @Deprecated
    # USE_PROXY(305, "Use Proxy"),
    # # https://tools.ietf.org/html/rfc7231#section-6.4.7">HTTP/1.1: Semantics and Content, section 6.4.7</a>
    # TEMPORARY_REDIRECT(307, "Temporary Redirect"),
    # # https://tools.ietf.org/html/rfc7238">RFC 7238</a>
    # PERMANENT_REDIRECT(308, "Permanent Redirect"),

    # // --- 4xx Client Error ---

    # # https://tools.ietf.org/html/rfc7231#section-6.5.1">HTTP/1.1: Semantics and Content, section 6.5.1</a>
    # BAD_REQUEST(400, "Bad Request"),
    # # https://tools.ietf.org/html/rfc7235#section-3.1">HTTP/1.1: Authentication, section 3.1</a>
    # UNAUTHORIZED(401, "Unauthorized"),
    # # https://tools.ietf.org/html/rfc7231#section-6.5.2">HTTP/1.1: Semantics and Content, section 6.5.2</a>
    # PAYMENT_REQUIRED(402, "Payment Required"),
    # # https://tools.ietf.org/html/rfc7231#section-6.5.3">HTTP/1.1: Semantics and Content, section 6.5.3</a>
    # FORBIDDEN(403, "Forbidden"),
    # # https://tools.ietf.org/html/rfc7231#section-6.5.4">HTTP/1.1: Semantics and Content, section 6.5.4</a>
    # NOT_FOUND(404, "Not Found"),
    # # https://tools.ietf.org/html/rfc7231#section-6.5.5">HTTP/1.1: Semantics and Content, section 6.5.5</a>
    # METHOD_NOT_ALLOWED(405, "Method Not Allowed"),
    # # https://tools.ietf.org/html/rfc7231#section-6.5.6">HTTP/1.1: Semantics and Content, section 6.5.6</a>
    # NOT_ACCEPTABLE(406, "Not Acceptable"),
    # # https://tools.ietf.org/html/rfc7235#section-3.2">HTTP/1.1: Authentication, section 3.2</a>
    # PROXY_AUTHENTICATION_REQUIRED(407, "Proxy Authentication Required"),
    # # https://tools.ietf.org/html/rfc7231#section-6.5.7">HTTP/1.1: Semantics and Content, section 6.5.7</a>
    # REQUEST_TIMEOUT(408, "Request Timeout"),
    # # https://tools.ietf.org/html/rfc7231#section-6.5.8">HTTP/1.1: Semantics and Content, section 6.5.8</a>
    # CONFLICT(409, "Conflict"),
    # # https://tools.ietf.org/html/rfc7231#section-6.5.9">
    # GONE(410, "Gone"),
    # # https://tools.ietf.org/html/rfc7231#section-6.5.10">
    # LENGTH_REQUIRED(411, "Length Required"),
    # # https://tools.ietf.org/html/rfc7232#section-4.2">
    # PRECONDITION_FAILED(412, "Precondition Failed"),
    # # https://tools.ietf.org/html/rfc7231#section-6.5.11">
    # PAYLOAD_TOO_LARGE(413, "Payload Too Large"),
    # # https://tools.ietf.org/html/rfc2616#section-10.4.14">HTTP/1.1, section 10.4.14</a>
    # REQUEST_ENTITY_TOO_LARGE(413, "Request Entity Too Large"),
    # # https://tools.ietf.org/html/rfc7231#section-6.5.12">
    # URI_TOO_LONG(414, "URI Too Long"),
    # # https://tools.ietf.org/html/rfc2616#section-10.4.15">HTTP/1.1, section 10.4.15</a>
    # REQUEST_URI_TOO_LONG(414, "Request-URI Too Long"),
    # # https://tools.ietf.org/html/rfc7231#section-6.5.13">
    # UNSUPPORTED_MEDIA_TYPE(415, "Unsupported Media Type"),
    # # https://tools.ietf.org/html/rfc7233#section-4.4">HTTP/1.1: Range Requests, section 4.4</a>
    # REQUESTED_RANGE_NOT_SATISFIABLE(416, "Requested range not satisfiable"),
    # # https://tools.ietf.org/html/rfc7231#section-6.5.14">
    # EXPECTATION_FAILED(417, "Expectation Failed"),
    # # https://tools.ietf.org/html/rfc4918#section-11.2">WebDAV</a>
    # UNPROCESSABLE_ENTITY(422, "Unprocessable Entity"),
    # # https://tools.ietf.org/html/rfc4918#section-11.3">WebDAV</a>
    # LOCKED(423, "Locked"),
    # # https://tools.ietf.org/html/rfc4918#section-11.4">WebDAV</a>
    # FAILED_DEPENDENCY(424, "Failed Dependency"),
    # # https://tools.ietf.org/html/rfc8470">RFC 8470</a>
    # TOO_EARLY(425, "Too Early"),
    # # https://tools.ietf.org/html/rfc2817#section-6">Upgrading to TLS Within HTTP/1.1</a>
    # UPGRADE_REQUIRED(426, "Upgrade Required"),
    # # https://tools.ietf.org/html/rfc6585#section-3">Additional HTTP Status Codes</a>
    # PRECONDITION_REQUIRED(428, "Precondition Required"),
    # # https://tools.ietf.org/html/rfc6585#section-4">Additional HTTP Status Codes</a>
    # TOO_MANY_REQUESTS(429, "Too Many Requests"),
    # # https://tools.ietf.org/html/rfc6585#section-5">Additional HTTP Status Codes</a>
    # REQUEST_HEADER_FIELDS_TOO_LARGE(431, "Request Header Fields Too Large"),
    # # https://tools.ietf.org/html/draft-ietf-httpbis-legally-restricted-status-04">
    #     * @since 4.3
    #     */
    # UNAVAILABLE_FOR_LEGAL_REASONS(451, "Unavailable For Legal Reasons"),

    # // --- 5xx Server Error ---

    # # https://tools.ietf.org/html/rfc7231#section-6.6.1">HTTP/1.1: Semantics and Content, section 6.6.1</a>
    # INTERNAL_SERVER_ERROR(500, "Internal Server Error"),
    # # https://tools.ietf.org/html/rfc7231#section-6.6.2">HTTP/1.1: Semantics and Content, section 6.6.2</a>
    # NOT_IMPLEMENTED(501, "Not Implemented"),
    # # https://tools.ietf.org/html/rfc7231#section-6.6.3">HTTP/1.1: Semantics and Content, section 6.6.3</a>
    # BAD_GATEWAY(502, "Bad Gateway"),
    # # https://tools.ietf.org/html/rfc7231#section-6.6.4">HTTP/1.1: Semantics and Content, section 6.6.4</a>
    # SERVICE_UNAVAILABLE(503, "Service Unavailable"),
    # # https://tools.ietf.org/html/rfc7231#section-6.6.5">HTTP/1.1: Semantics and Content, section 6.6.5</a>
    # GATEWAY_TIMEOUT(504, "Gateway Timeout"),
    # # https://tools.ietf.org/html/rfc7231#section-6.6.6">HTTP/1.1: Semantics and Content, section 6.6.6</a>
    # HTTP_VERSION_NOT_SUPPORTED(505, "HTTP Version not supported"),
    # # https://tools.ietf.org/html/rfc2295#section-8.1">Transparent Content Negotiation</a>
    # VARIANT_ALSO_NEGOTIATES(506, "Variant Also Negotiates"),
    # # https://tools.ietf.org/html/rfc4918#section-11.5">WebDAV</a>
    # INSUFFICIENT_STORAGE(507, "Insufficient Storage"),
    # # https://tools.ietf.org/html/rfc5842#section-7.2">WebDAV Binding Extensions</a>
    # LOOP_DETECTED(508, "Loop Detected"),
    # /**
    #     * {@code 509 Bandwidth Limit Exceeded}
    #     */
    # BANDWIDTH_LIMIT_EXCEEDED(509, "Bandwidth Limit Exceeded"),
    # # https://tools.ietf.org/html/rfc2774#section-7">HTTP Extension Framework</a>
    # NOT_EXTENDED(510, "Not Extended"),
    # # https://tools.ietf.org/html/rfc6585#section-6">Additional HTTP Status Codes</a>
    # NETWORK_AUTHENTICATION_REQUIRED(511, "Network Authentication Required");


class DelegateHttpRequest:
    option: O
    @property
    def url(self):
        return self.option._base_.source.host + self.option._http_.path
    @property
    def header(self):
        return self.option._http_.header
    
    @abstractmethod
    def get(self, urlParams: Optional[Dict[str, str]]) -> any:
        raise NotImplementedError
    
    @abstractmethod
    def post(self, urlParams: Optional[Dict[str, str]], body: Optional[Union[str, dict]]):
        raise NotImplementedError
    
    def __init__(self, option: O):
        self.option = option


class DelegateAsyncHttpRequest:
    option: O
    def url(self, urlParams: Optional[Dict[str, str]] = None):
        if urlParams:
            serialized_params = '&'.join(['{}={}'.format(k, v) for k, v in urlParams.items()])
            return '{}{}?{}'.format(self.option._base_.source.host, self.option._http_.path, serialized_params)
        return self.option._base_.source.host + self.option._http_.path
    @property
    def header(self):
        return self.option._http_.header
    
    @abstractmethod
    async def get(self, urlParams: Optional[Dict[str, str]]) -> any:
        raise NotImplementedError
    
    @abstractmethod
    async def post(self, urlParams: Optional[Dict[str, str]], body: Optional[Union[str, dict]]):
        raise NotImplementedError
    
    def __init__(self, option: O):
        self.option = option


R = TypeVar('R', bound=DelegateHttpRequest)
AR = TypeVar('AR', bound=DelegateHttpRequest)


class HttpDelegate(IoDelegate[E, RO, WO], Generic[E, RO, WO]):
    Entity: Type[E] = None
    ReadOption: Type[RO] = None
    WriteOption: Type[WO] = None
    
    @abstractmethod
    def _build_request(self, option: O) -> R:
        raise NotImplementedError
    def _build_async_request(self, option: O) -> AR:
        raise NotImplementedError
    
    # @abstractmethod
    def _do_write(self, request: R, option: WO = None) -> any:
        raise NotImplementedError
    # @abstractmethod
    def _do_read(self, request: R, option: RO = None) -> any:
        raise NotImplementedError
    
    def _pre_read(self, option: RO = None) -> Optional[E]:
        return None
    def read(self, option: RO = None) -> Optional[E]:
        r = self._pre_read(option)
        if r:
            return r
        request = self._build_request(option)
        result = self._do_read(request, option)
        if isinstance(result, Entity):
            # 子类自己实现了 sink.content 类似的功能, 直接返回了
            return result
        # 否则, 父类来帮你
        sink = IoReadSink(self.__class__, option._base_.source, result)
        # 父类允许子类其他骚操作
        return self._post_read(sink.content, option)
    def _post_read(self: T, entity: E, option: RO) -> E:
        return entity

    def write(self, option: WO = None) -> any:
        request = self._build_request(option)
        return self._do_write(request, option)
    
    # ---------------------------- async ----------------------------
    
    async def async_write(self, option: WO = None) -> any:
        request = self._build_async_request(option)
        return await self._do_async_write(request, option)
    async def _do_async_write(self, request: AR, option: WO = None) -> any:
        raise NotImplementedError
    async def async_read(self, option: RO = None) -> Optional[E]:
        r = self._pre_read(option)
        if r:
            return r
        request = self._build_async_request(option)
        result = await self._do_async_read(request, option)
        if isinstance(result, Entity):
            # 子类自己实现了 sink.content 类似的功能, 直接返回了
            return result
        # 否则, 父类来帮你
        sink = IoReadSink(self.__class__, option._base_.source, result)
        # 父类允许子类其他骚操作
        return self._post_read(sink.content, option)
    async def _do_async_read(self, request: AR, option: RO = None) -> any:
        raise NotImplementedError
