from typing import Optional, TypeVar
from .converter import Converter
from ..typing import Schema, Schemable
from ...share.entity import Entity


T = TypeVar('T', bound=Entity)


class SchemablePython(Schemable):
    __schema__ = None

    @classmethod
    def _do_from_dict(clazz,
                      from_dict: dict,
                      schema: Optional[Schema] = None,
                      **kargs) -> Optional[T]:
        if not clazz.__schema__ and not schema:
            raise NotImplementedError
        from_dict = clazz.pre_schema(from_dict, **kargs)
        if not from_dict:
            return None
        instance = Converter.instance().convert(from_dict, schema or clazz.__schema__, clazz)
        return clazz.post_schema(from_dict, instance, **kargs)

    @classmethod
    def pre_schema(clazz,
                   from_dict: dict,
                   **kargs) -> Optional[dict]:
        return from_dict

    @classmethod
    def post_schema(clazz,
                    from_dict: dict,
                    instance: T,
                    **kargs) -> Optional[T]:
        return instance
