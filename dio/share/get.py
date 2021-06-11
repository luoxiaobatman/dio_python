from typing import Dict, List, Tuple, Union
from .entity import Entity


def get(o: Union[Dict, List, Entity], keys: Union[str, int, List[Union[str, int]]], default=None) -> any:
    if not isinstance(keys, (List, Tuple)):
        keys = [keys]
    for key in keys:
        try:
            if isinstance(o, (Dict, List, Tuple)):
                o = o[key]
            else:
                o = getattr(o, key)
        except Exception:
            return default
    if o is None:
        return default
    return o
