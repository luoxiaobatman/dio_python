import asyncio
from typing import Dict, List
from dio.share.entity import Entity
from impl.delegate_memory_noop import DelegateMemoryNoop
from impl.delegate_javap_aiohttp import DelegateJavapAioHttp, ReadOptionJavapAioHttp


class Baz(Entity):
    baz: str


class Bar(Entity):
    bar_0: str
    bar_1: Baz


class Foo(Entity):
    foo_0: str
    foo_1: Bar
    foo_2: List[Bar]
    foo_3: Dict[str, Bar]


if __name__ == '__main__':
    pass