from typing import Union
from ..mixin.jsonable import Jsonable


class Entity(Jsonable):
    id: Union[int, str, None]
    
    