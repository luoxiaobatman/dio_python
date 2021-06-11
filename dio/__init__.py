from logging import Logger

from .schemable.schemable_python.compiler import compile_schema
from .schemable.schemable_python.schemable_python import SchemablePython
from .schemable.schemable_python.converter import Converter
from .schemable.typing import Schemable

from .delegate.abstract.http_delegate import DelegateHttpRequest, HttpDelegate, DelegateAsyncHttpRequest
from .delegate.abstract.redis_delegate import RedisDelegate
from .delegate.typing import IoDelegate
from .delegate.core.io_read_sink import IoReadSink
from .delegate.core.io_source import IoSource, IoSourceRedis
from .delegate.core.option_http import OptionHttp
from .delegate.core.option_base import OptionBase
from .delegate.core.option_redis import OptionRedis

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
v0.0.4+
    独立模块  √
    单元测试
    exception handling
    整合fileio
    整合redis  √
    async
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
    # 'Schema',
    'Schemable',
    'SchemablePython',
    'compile_schema',  # TODOlx 不暴露
    'Converter',
    'Entity',
    
    'IoDelegate',
    'HttpDelegate',
    'RedisDelegate',
    'DelegateHttpRequest',
    'DelegateAsyncHttpRequest',
    'OptionHttp',
    'OptionRedis',
    'IoSource',
]
