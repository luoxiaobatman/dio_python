"""
TODO localcache
"""
import time
from abc import abstractmethod
from typing import Dict, Optional
from ...share import Entity


class CacheEntry:
    expire_at: int
    val: Entity
    
    def hit():
        return None


CACHE: Dict[str, Dict[str, CacheEntry]] = {}


class _LocalCache_:
    ttl: int  # 毫秒
    def __init__(self, ttl: int) -> None:
        self.ttl = ttl


class OptionLocalCache:
    _local_cache_: _LocalCache_  # 毫秒
    def __init__(self, ttl: int = None) -> None:
        self._local_cache_ = _LocalCache_(ttl)


class DelegateLocalCache:
    @abstractmethod
    def _local_cache_keygen(self) -> str:
        raise NotImplementedError
    def _domain_name(self) -> str:
        return str(self.__class__)
        
    # def _pre_read(self, option: OptionLocalCache) -> Optional[Entity]:
    #     now = int(time.time() * 1000)
    #     if isinstance(option, OptionLocalCache):
    #         domain_name = self._domain_name()
    #         if domain_name not in CACHE:
    #             CACHE[domain_name] = {}
    #         domain = CACHE[domain_name]
    #         key = self._local_cache_keygen()
    #         if key in domain:
    #             cache_entry = domain[key]
    #             if cache_entry.expire_at < now
                
    #         if key in CACHE
    #     return None
