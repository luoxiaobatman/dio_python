from dio.share.entity import Entity
from typing import List, Optional


class FlagOption(Entity):
    ouid: int  # 博主
    sid: int
    option: int
    label: str
    cuid: Optional[int]  # 用户
    delta: Optional[int]  # 用户对count的贡献量, 0为没有贡献
    count: Optional[int]
    
    
class FlagStats(Entity):
    uid: int
    sid: int
    options: List[FlagOption]


class EntityFlagStatsBatch(Entity):
    batch: List[FlagStats]


class FlagUserInteract(Entity):
    uid: int
    options: List[FlagOption]
