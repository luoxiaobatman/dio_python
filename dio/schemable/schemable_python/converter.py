from typing import Type, TypeVar, Union, List, Dict
from ..typing import Schema, Schemable
from ...share.entity import Entity
from ...share.get import get
from ...mixin.immutable import Immutable
from ...mixin.logging import Logging


# T = TypeVar('T', bound=IoDelegate)  converter应该是IoDelegateConverter
T = TypeVar('T')


Converter = None


class Converter(Immutable, Logging):
    @staticmethod
    def instance() -> Converter:
        return _converter_
    
    def dict_to_dict(self, from_dict: dict, schema: Dict):
        to_dict = {}
        for schema_k, schema_v in schema.items():
            if isinstance(schema_v, dict):
                to_dict[schema_k] = self.dict_to_dict(from_dict, schema_v)
            elif isinstance(schema_v, str):
                to_dict[schema_k] = get(from_dict, schema_v)
            elif isinstance(schema_v, (list, tuple)):
                value = None
                keyss = schema_v[0]
                default_value = schema_v[1]
                transform = schema_v[2]
                exceptions_and_values = schema_v[3]
                args = []
                try:
                    for keys, dv in zip(keyss, default_value):
                        args.append(get(from_dict, keys, dv))
                    value = transform(*args) if transform else args[0]
                except Exception as e:
                    self.logger.info('DICT_TO_DICT_CONVERT, schema=%s, args=%s', {schema_k: schema_v}, args)
                    raise_to_caller_of_this_stack = True
                    if exceptions_and_values:
                        for exception_class, default_return_value in exceptions_and_values:
                            if isinstance(e, exception_class):
                                value = default_return_value
                                raise_to_caller_of_this_stack = False
                                break
                    if raise_to_caller_of_this_stack:
                        raise
                to_dict[schema_k] = value
            else:
                raise Exception('unsupportted')
        return to_dict
        
    def convert(self, from_dict: dict, schema: Schema, clazz: Type[T]) -> T:
        if hasattr(clazz, 'Entity') and issubclass(clazz.Entity, Entity):
            clazz = clazz.Entity
        instance = clazz()
        # 父亲先解
        to_dict = self.dict_to_dict(from_dict, schema._schema)
        # ---------------------------- 再解孩子 START ----------------------------
        if schema._child_mapping:
            for k, v in schema._child_mapping.items():
                child_from_dict: Union[List, Dict, None] = get(from_dict, v[0][0], v[1][0])
                if not v[4](child_from_dict):
                    continue
                schema_or_schemable = v[2]
                # ---------------------------- 推断孩子的runtime_clazz(subclass of Schemable), 用实体__annotations__判定是否需要解list START ----------------------------
                runtime_clazz: Schemable = None
                try:
                    is_subclass_of_Schemable = issubclass(schema_or_schemable, Schemable)
                except Exception:
                    is_subclass_of_Schemable = False
                if is_subclass_of_Schemable:
                    schema = schema_or_schemable.__schema__
                    runtime_clazz = schema_or_schemable
                annotated_clazz = clazz.__annotations__[k]
                is_list = str(annotated_clazz).startswith('typing.List')  # List类型检查
                if runtime_clazz is None:
                    if is_list:
                        runtime_clazz = annotated_clazz.__args__[0]
                    else:
                        runtime_clazz = annotated_clazz
                # ---------------------------- 推断孩子的runtime_clazz, 用实体__annotations__判定是否需要解list END ----------------------------
                try:
                    # ---------------------------- 解 START ----------------------------
                    if is_list:
                        if isinstance(child_from_dict, list):
                            # TODOlx child_from_dict类型还需要进一步推断
                            to_dict[k] = runtime_clazz.from_list_of_dict(child_from_dict)
                        else:
                            to_dict[k] = None
                    else:
                        to_dict[k] = runtime_clazz.from_dict(child_from_dict)
                    # ---------------------------- 解 END ----------------------------
                except Exception as e:
                    self.logger.info('DICT_TO_DICT_CONVERT, schema=%s, args=%s', {k: v}, from_dict)
                    raise_to_caller_of_this_stack = True
                    exceptions_and_values = v[3]
                    if exceptions_and_values:
                        for exception_class, default_return_value in exceptions_and_values:
                            if isinstance(e, exception_class):
                                to_dict[k] = default_return_value
                                raise_to_caller_of_this_stack = False
                                break
                    if raise_to_caller_of_this_stack:
                        raise
        # ---------------------------- 再解孩子 END ----------------------------
        if hasattr(instance, '__dict__'):
            instance.__dict__.update(to_dict)
        elif hasattr(instance, '__slots__'):
            for slot in instance.__slots__:
                instance.__setattr__(slot, to_dict.get(slot))
        else:
            raise Exception('fill_instance error')
        return instance


_converter_ = Converter()
