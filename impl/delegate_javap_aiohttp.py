from dio.share.entity import Entity
from dio.delegate.core.option.option_http import OptionHttp
from dio.delegate.abstract.aiohttp_delegate import AioHttpDelegate, AioHttpRequest
from dio.delegate.core.source.source_base import SourceBase
from dio.schemable.schemable_python.compiler import compile_schema


class Foo(Entity):
    foo: int


schema = compile_schema({
    'foo': 'foo',
})


class SourceLocalhost7390(SourceBase):
    def content(self, schemable_clz, data, schema):
        return schemable_clz.from_json(data, schema)


class ReadOptionJavapAioHttp(OptionHttp):
    def __init__(self):
        super().__init__(
            source=SourceLocalhost7390('http://localhost:7390'),
            schema=schema,
            path='/foo',
            header=None,
        )


class DelegateJavapAioHttp(AioHttpDelegate):
    Entity = Foo
    ReadOption = ReadOptionJavapAioHttp

    async def _do_read(self, request: AioHttpRequest, ro: ReadOptionJavapAioHttp):
        return await request.post(None, None)
    async def _do_write(self, request: AioHttpRequest, wo):
        raise NotImplementedError
