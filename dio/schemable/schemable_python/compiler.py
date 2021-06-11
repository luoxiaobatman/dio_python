import json
from ..typing import _Schema, Schema, Schemable


def compile_schema(schema: _Schema) -> Schema:
    compiled_schema = Schema()
    compiled_schema_inner_dict = {}
    compiled_schema._schema = compiled_schema_inner_dict
    _child_mapping = {}
    compiled_schema._child_mapping = _child_mapping

    def wrap_exception(k, message) -> Exception:
        d = {}
        if isinstance(message, str):
            d = {k: message}
        elif isinstance(message, Exception):
            d = {k: json.loads(str(message))}
        return Exception(json.dumps(d))

    def recursive_compile(k, schema, compiled_schema_inner_dict, child_mapping, level):
        def compile_keyss(keyss, default_value):
            if not isinstance(keyss, (str, list, tuple)):
                raise wrap_exception(k, 'the 0th only str or (list, tuple)')

            if isinstance(keyss, str):
                return [keyss]
            elif not isinstance(default_value, (list, tuple)):
                raise wrap_exception(k, 'if the 0th is (list, tuple), then the 1st must be (list, tuple)')
            return keyss

        if not isinstance(schema, (str, dict, list, tuple, Schema)):
            raise wrap_exception(k, 'is not dict or list or tuple')

        if isinstance(schema, dict):
            child_schema = {}
            compiled_schema_inner_dict[k] = child_schema
            next_level_child_mapping = {}
            child_mapping[k] = next_level_child_mapping
            for k0, v0 in v.items():
                try:
                    recursive_compile(k0, v0, child_schema, level + 1)
                except Exception as e:
                    raise wrap_exception(k0, e)
            if not next_level_child_mapping:
                del child_mapping[k]

        if isinstance(schema, str):
            compiled_schema_inner_dict[k] = schema

        if isinstance(schema, (list, tuple)):
            is_a_wrapper_for_another_schema = False
            if len(schema) == 0:
                raise wrap_exception(k, 'len should be greater than 0')

            keyss = schema[0]
            try:
                default_value = schema[1]
            except Exception:
                default_value = None
            compiled_keyss = compile_keyss(keyss, default_value)
            compiled_list = [compiled_keyss, [None] * len(keyss), None, [(Exception, None)], lambda x: True]
            if len(schema) > 1:
                default_value = schema[1]
                if isinstance(keyss, (list, tuple)):
                    if not isinstance(default_value, (list, tuple)):
                        raise wrap_exception(k, 'the 1st default value should also be (list, tuple)')
                    if len(keyss) != len(default_value):
                        raise wrap_exception(k, 'the 1st default value and keyss should be the same len')
                if isinstance(keyss, str):
                    default_value = [default_value]
                compiled_list[1] = default_value
                if len(schema) > 2:
                    transform = schema[2]
                    try:
                        is_subclass_of_Schemable = issubclass(transform, Schemable)
                    except Exception:
                        is_subclass_of_Schemable = False
                    if isinstance(transform, Schema) or (isinstance(transform, list) and isinstance(transform[0], Schema)) or is_subclass_of_Schemable:
                        if level > 0:
                            raise wrap_exception(k, 'for now, child schema is not supported belong level 0 dict')
                        if isinstance(compiled_list[0][0], str):
                            compiled_list[0][0] = [compiled_list[0][0]]
                        compiled_list[2] = transform
                        is_a_wrapper_for_another_schema = True
                    elif callable(transform):
                        compiled_list[2] = transform
                    else:
                        raise wrap_exception(k, 'the 2rd transform should be callable or Schema or Schemable_Type')

                    if len(schema) > 3:
                        exceptions_and_values = schema[3]
                        if not isinstance(exceptions_and_values, (list, tuple)):
                            raise wrap_exception(k, 'the 3rt exceptions and values should be (list, tuple)')
                        for exceptions_and_values_item in exceptions_and_values:
                            if not isinstance(exceptions_and_values_item, (list, tuple)):
                                raise wrap_exception(k, 'the 3rt exceptions and values item should be (list, tuple)')
                            if len(exceptions_and_values_item) != 2:
                                raise wrap_exception(k, 'the 3rt exceptions and values item should len = 2')
                            if not issubclass(exceptions_and_values_item[0], Exception):
                                raise wrap_exception(k, 'the 3rt exceptions and values should be subclass of Exception')
                        compiled_list[3] = exceptions_and_values
                    if len(schema) > 4:
                        ignorer = schema[4]
                        if callable(ignorer):
                            compiled_list[4] = ignorer
                        else:
                            raise wrap_exception(k, 'the 4rt ignore function should be callable')
            if is_a_wrapper_for_another_schema:
                child_mapping[k] = compiled_list
            else:
                compiled_schema_inner_dict[k] = compiled_list

        if isinstance(schema, Schema):
            compiled_list = [[k], [None], schema, [(Exception, None)], lambda x: True]
            child_mapping[k] = compiled_list

    if not isinstance(schema, dict):
        raise Exception('schema should be a dict')

    for k, v in schema.items():
        recursive_compile(k, v, compiled_schema_inner_dict, _child_mapping, 0)
    return compiled_schema
