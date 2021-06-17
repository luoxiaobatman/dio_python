import json
from typing import Type, TypeVar, Dict, List, Union
from ..share.get import get

E = TypeVar('E')
primaries = (int, str, bool)


def get_contained_clz(container):
    return container.__args__[-1]


def _all_annotations(clz):
    if not hasattr(clz, '__all_annotations__'):
        d = {}
        for c in clz.mro():
            try:
                d.update(**c.__annotations__)
            except AttributeError:
                pass
        clz.__all_annotations__ = d
    return clz.__all_annotations__


class Jsonable:
    """
    TODO
    container封装只支持dict和list, 不支持循环嵌套, 且dict封装只支持str作为key
    bool, str, int
    """
    @classmethod
    def loads(clz: Type[E], json_or_dict: Union[str, Dict]) -> E:
        a_dict = json_or_dict
        if isinstance(a_dict, str):
            a_dict = json.loads(a_dict)
        
        entity = clz()
        
        annotations = _all_annotations(clz)
        
        for k, clz_annotated in annotations.items():
            data = get(a_dict, k, None)
            if data is not None:
                if clz_annotated in primaries:
                    setattr(entity, k, data)
                elif hasattr(clz_annotated, '_name') and clz_annotated._name == 'List':
                    clz_annotated = get_contained_clz(clz_annotated)
                    if clz_annotated in primaries:
                        setattr(entity, k, data)
                    else:
                        setattr(entity, k, [clz_annotated.loads(item) for item in data])
                elif hasattr(clz_annotated, '_name') and clz_annotated._name == 'Dict':
                    clz_annotated = get_contained_clz(clz_annotated)
                    if clz_annotated in primaries:
                        setattr(entity, k, data)
                    else:
                        setattr(entity, k, {data_k: clz_annotated.loads(data_v) for data_k, data_v in data.items()})
                else:
                    setattr(entity, k, clz_annotated.loads(data))
            else:
                setattr(entity, k, None)
        return entity
        
    def dumps(self) -> str:
        return json.dumps(self._dumps())

    def _dumps(self) -> Dict:
        result = {**self.__dict__}
        
        annotations = _all_annotations(self.__class__)
        
        for k, clz_annotated in annotations.items():
            data = getattr(self, k, None)
            if data is not None:
                if clz_annotated in primaries:
                    pass
                elif hasattr(clz_annotated, '_name') and clz_annotated._name == 'List':
                    clz_annotated = get_contained_clz(clz_annotated)
                    if clz_annotated in primaries:
                        pass
                    else:
                        result[k] = [item._dumps() for item in data]
                elif hasattr(clz_annotated, '_name') and clz_annotated._name == 'Dict':
                    clz_annotated = get_contained_clz(clz_annotated)
                    if clz_annotated in primaries:
                        pass
                    else:
                        result[k] = {item_k: item_v._dumps() for item_k, item_v in data.items()}
                else:
                    result[k] = data._dumps()
        return result
