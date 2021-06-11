from abc import abstractmethod
from typing import Dict, TypeVar, List, Tuple, Callable, Union, Optional, Iterable
import json

from ..share.entity import Entity


_Schema = None  # decl, 用Generic可以解决自引用的问题, 但还没想好怎么用
Schema = None

"""
#0 keyss, 当为List类型时, 长度可变, 需要cotyping #1, #2, #3. 没找到好办法, 
   写了个compiler初始化运行时校验, typing模块里面的Protocol可能会是有用
#1 keys's default value
#2 transformer
#3 catch exception and default value
"""
_L = Tuple[
    Union[str, List[Union[str, Tuple[str]]]],  #0
    Union[object, List[object]],  #1
    Union[Callable, Schema],  #2 
    List[Tuple[Exception, object]],  #3
]
_SELF = Union[str, _Schema, _L]
_Schema = Dict[str, _SELF]


class Schema:
    _child_mapping: Dict[str, _Schema]
    _schema: _Schema


T = TypeVar('T', bound=Entity)


class Schemable:
    __schema__ = None
    @classmethod
    def from_dict(clazz,
                  data: dict,
                  schema: Optional[Schema] = None,
                  **kargs: Optional[Dict]) -> Optional[T]:
        return clazz._do_from_dict(data, schema, **kargs)

    @classmethod
    def from_json(clazz,
                  data: str,
                  schema: Optional[Schema] = None,
                  **kargs: Optional[Dict]) -> Optional[T]:
        data = json.loads(data)
        return clazz.from_dict(data, schema, **kargs)

    @classmethod
    def from_list_of_dict(clazz,
                          data: List[dict],
                          schema: Optional[Schema] = None,
                          **kargs: Optional[Dict]) -> List[T]:
        if isinstance(data, list):
            return [clazz.from_dict(d, schema, **kargs) for d in data]
        return []

    @classmethod
    def from_iterable_of_string(clazz,
                                data: Iterable[str],
                                schema: Optional[Schema] = None,
                                **kargs: Optional[Dict]) -> List[T]:
        if isinstance(data, Iterable):
            return [clazz.from_json(d, schema, **kargs) for d in data if isinstance(d, str)]
        return []

    @classmethod
    @abstractmethod
    def _do_from_dict(clazz,
                      from_dict: dict,
                      schema: Optional[Schema] = None,
                      **kargs) -> Optional[T]:
        raise NotImplementedError
