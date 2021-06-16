from typing import Dict, Optional, Union
import aiohttp
from .http_delegate import HttpRequest, HttpDelegate


class AioHttpRequest(HttpRequest):
    async def get(self, urlParams: Optional[Dict[str, str]]) -> str:
        async with aiohttp.ClientSession() as client:
            async with client.get(self.url(urlParams), headers=self.header) as resp:
                return await resp.text()
    async def post(self, urlParams: Optional[Dict[str, str]], body: Optional[Union[str, dict]]) -> str:
        async with aiohttp.ClientSession() as client:
            async with client.post(self.url(urlParams), data=body, headers=self.header) as resp:
                return await resp.text()


class AioHttpDelegate(HttpDelegate):
    def _build_request(self, option) -> AioHttpRequest:
        return AioHttpRequest(option)
