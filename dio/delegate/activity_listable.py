from typing import Optional
from time import time
from redis import Redis

from dio import SchemablePython, compile_schema, OptionRedis, RedisDelegate

from api_base.logger import logger
from api_base.cache import redis

from ..entity import EntityActivity, EntityActivityListable
from ..source.redis import io_source_redis


class DelegateActivity(EntityActivity, SchemablePython):
    __schema__ = compile_schema({
        'id': 'id',
        'name': 'name',
        'link': 'link',
        'version': 'version',
        'pid': 'pid',
        'icon': 'icon',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'position_id': (
            'position_id',
            201,
        ),
        'user_tag_id': 'user_tag_id',
        'rank': (
            'rank',
            0,
        ),
        'platform': 'platform'
    })


class ReadOption(OptionRedis):
    def __init__(self) -> None:
        super().__init__(client=redis, source=io_source_redis)
    # ---------------------------- 命令 START ----------------------------
    
    # ---------------------------- 命令 END ----------------------------
    

class DelegateActivityListable(EntityActivityListable, RedisDelegate):
    __schema__ = compile_schema({
        'list': ('list', None, DelegateActivity),
    })
    
    def _pre_read(self, option: ReadOption) -> Optional[EntityActivityListable]:
        return option._localcache_.read()
    def _do_read(self, client: Redis, *args, **kargs) -> any:
        K_ZEND = 'activity:zsetend'
        K_ZSTART = 'activity:zsetstart'
        if client.exists(K_ZEND, K_ZSTART) != 2:
            logger.info('[RELOAD NEEDED] activity')
            return None
        unixtime = int(time())
        end_ids = client.zrangebyscore(K_ZEND, unixtime, (1 << 64) - 1)
        if not end_ids:
            return None
        start_ids = set(client.zrangebyscore(K_ZSTART, 0, unixtime))
        intersection = set(end_ids).intersection(start_ids)
        if not intersection:
            return None
        # r = client.hmget('activity:info', intersection)
        return {'list': client.hmget('activity:info', intersection)}
    def _post_read(self, entity: EntityActivityListable, option: ReadOption) -> EntityActivityListable:
        option._localcache_.write(entity)
        return entity
