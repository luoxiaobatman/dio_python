import asyncio
from impl.delegate_memory_noop import DelegateMemoryNoop
from impl.delegate_javap_aiohttp import DelegateJavapAioHttp, ReadOptionJavapAioHttp


if __name__ == '__main__':
    ro = ReadOptionJavapAioHttp()
    wo = None
    
    loop = asyncio.new_event_loop()
    Chained = DelegateJavapAioHttp.fork([(DelegateMemoryNoop, None, None)])
    foo = loop.run_until_complete(Chained().flow(ro, wo))
    print(foo)
