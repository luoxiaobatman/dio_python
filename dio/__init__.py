from logging import Logger

from .schemable.schemable_python.compiler import compile_schema
from .schemable.schemable_python.schemable_python import SchemablePython
from .schemable.schemable_python.converter import Converter
from .schemable.typing import Schemable

from .delegate.abstract.http_delegate import HttpRequest, HttpDelegate
from .delegate.abstract.aiohttp_delegate import AioHttpDelegate, AioHttpRequest
from .delegate.typing import IoDelegate
from .delegate.core.option.option_base import OptionBase
from .delegate.core.option.option_http import OptionHttp
from .delegate.core.source.source_base import SourceBase
from .delegate.impl.delegate_memory_noop import DelegateMemoryNoop

from .share.entity import Entity
from .registration import Registration


"""
v0.0.1
    compiler, converter, schemable  √
v0.0.2
    迁移user, poi, abtest等初步验证  √
v0.0.3
    实现并验证了整合io想法  √
    整合http, 采用PoolHttpClient实现  √
    迁移user_setting  √ 
    迁移picture  √
v0.0.4
    独立模块  √
    async √
v0.0.5
    私有 √
v0.1.0
    flow
长期规划
    http实现
    compiler language agnostic
"""

registered = False


def register_dio(logger: Logger):
    """
    called at most once
    """
    global registered
    if registered:
        """
        TODO
        """
        raise Exception
    Registration.register(logger)
    registered = True
    

__all__ = [
    # schemable暴露
    'Schemable',
    'SchemablePython',
    'compile_schema',  # TODOlx 不暴露
    'Converter',
    'Entity',
    
    # delegate暴露
    'HttpRequest',
    'HttpDelegate',
    'AioHttpDelegate',
    'AioHttpRequest',
    'IoDelegate',
    'OptionBase',
    'OptionHttp',
    'SourceBase',
    'DelegateMemoryNoop',
]
