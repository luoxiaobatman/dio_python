from typing import List, Dict
from dio.share.entity import Entity

from api_base.util.mixin import MixinResponsePostProcessor


class EntityActivity(Entity):
    id: int
    name: str
    link: str
    version: str
    pid: str
    start_time: int
    end_time: int
    position_id: int
    user_tag_id: int
    rank: int
    icon: str
    platform: int

    CACHE_FIELDS = ['platform']

    def __repr__(self):
        return f"ActivityEntity={getattr(self, 'id', 0)},name:{getattr(self, 'name','-')}"


class EntityActivityListable(Entity, MixinResponsePostProcessor):
    list: List[EntityActivity]
    next_cursor: str  # listable固有, 实际EntityActivity在业务上并不需要这些属性
    cursor: str  # listable固有, 实际EntityActivity在业务上并不需要这些属性
    count: int  # listable固有, 实际EntityActivity在业务上并不需要这些属性
    
    def _do_post_process_response(self, **kargs):
        self.cursor = None
        self.count = None
