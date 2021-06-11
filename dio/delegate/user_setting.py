import json
from typing import List
from time import time

from dio import compile_schema

from api_base.logger import logger, exception_logger, picture_download_logger
from api_base.cache import redis_topic
from api_base.util.oasisimgbed import get_user_background_url

from .abstract.pool_client_http_delegate import PoolClientHttpRequest, PoolClientHttpDelegate
from ..entity import EntityUserSetting
from ..constant import UserSettingKeyValueDef, UserSettingKey, UserSettingKeyDescriptor
from ..source.oasis_service import io_source_oasis_service
from ..option import PoolClientOptionHttp


ReadOption = None
WriteOption = None
KeyValueDef = UserSettingKeyValueDef
KeyDescriptor = UserSettingKeyDescriptor
Key = UserSettingKey


# ---------------------------- 读参数定义 START ----------------------------
class ReadOption(PoolClientOptionHttp):
    keys: List[KeyDescriptor]
    
    def __init__(self, keys: List[KeyDescriptor]):
        super().__init__(source=io_source_oasis_service, path='/user_settings/query')
        self.keys = keys
        
    @staticmethod
    def video_setting() -> ReadOption:
        return ReadOption([Key.video_cost, Key.video_cost_index, Key.available_video_costs, Key.video_forbidden])

    @staticmethod
    def picture_setting() -> ReadOption:
        return ReadOption([Key.picture_cost, Key.picture_cost_index, Key.available_picture_costs, Key.picture_forbidden])

    @staticmethod
    def privicy() -> ReadOption:
        return ReadOption([Key.show_f12, Key.show_me_in_city_channel, Key.allow_stranger_im])

    @staticmethod
    def auto_follow_topic_when_publish() -> ReadOption:
        return ReadOption([Key.auto_follow_topic_when_publish])

    @staticmethod
    def background() -> ReadOption:
        return ReadOption([Key.background_url, Key.background])

    @staticmethod
    def operator_push() -> ReadOption:
        return ReadOption([Key.operator_push])


class WriteOption(PoolClientOptionHttp):
    def __init__(self):
        super().__init__(source=io_source_oasis_service, path='/user_settings/upsert')


class DelegateUserSetting(EntityUserSetting, PoolClientHttpDelegate[EntityUserSetting, ReadOption, WriteOption]):
    def __init__(self, uid: int = None) -> None:
        self.uid = uid
    def write(self, option=WriteOption()) -> any:
        return super().write(option=option)
    
    Key = Key
    KeyValueDef = KeyValueDef
    KeyDescriptor = KeyDescriptor
    ReadOption = ReadOption
    WriteOption = WriteOption
    Entity = EntityUserSetting

    __schema__ = compile_schema({
        'sync_weibo_with_watermark': ('sync_weibo_with_watermark', Key.sync_weibo_with_watermark.default.value),
        'show_me_in_city_channel': ('show_me_in_city_channel', Key.show_me_in_city_channel.default.value),
        'picture_cost': ('picture_cost', Key.picture_cost.default.value),
        'picture_cost_index': ('picture_cost_index', Key.picture_cost_index.default.value),
        'video_cost': ('video_cost', Key.video_cost.default.value),
        'video_cost_index': ('video_cost_index', Key.video_cost_index.default.value),
        'default_recommend_position': ('default_recommend_position', Key.default_recommend_position.default.value),
        'background': ('background', Key.background.default.value, lambda x: x if x else Key.background.default.value),
        'background_url': ('background', Key.background.default.value, lambda x: get_user_background_url(x) if x else KeyValueDef.background_url_default.value),
        'auto_follow_topic_when_publish': ('auto_follow_topic_when_publish', Key.auto_follow_topic_when_publish.default.value),
        'show_f12': ('show_f12', Key.show_f12.default.value, lambda x: int(x)),
        'show_f10': ('show_f10', Key.show_f10.default.value, lambda x: int(x)),
        'allow_stranger_im': ('allow_stranger_im', Key.allow_stranger_im.default.value),
        'operator_push': ('operator_push', Key.operator_push.default.value),
        'fold_stranger_im': ('fold_stranger_im', Key.fold_stranger_im.default.value),
        'picture_forbidden': (
            'picture_cost',
            None,
            lambda x: x == KeyValueDef.picture_cost_forbidden.value,
            [(Exception, True)]
        ),
        'video_forbidden': (
            'video_cost',
            None,
            lambda x: x == KeyValueDef.video_cost_forbidden.value,
            [(Exception, True)]
        ),
    })
    
    def _do_read(self, request: PoolClientHttpRequest, option: ReadOption) -> any:
        assert self.uid
        serialized_keys = set()
        for k in option.keys:
            serialized_keys.add(k.serialized)
            if not k.standalone:
                for kk in k.depends:
                    serialized_keys.add(kk.serialized)
        try:
            return request.get({'uid': self.uid, 'keys': ','.join(serialized_keys)})['object']
        except Exception:
            logger.exception('query error!, Pls Check!')
            return {k.serialized: k.default.value for k in option.keys}

    def _post_read(self, entity: EntityUserSetting, option: ReadOption):
        r = EntityUserSetting()
        for k in option.keys:
            setattr(r, k.serialized, getattr(entity, k.serialized, k.default.value))
            if not k.standalone:
                for kk in k.depends:
                    setattr(r, kk.serialized, getattr(entity, kk.serialized, kk.default.value))
        return r
    
    def _do_write(self, request: PoolClientHttpRequest, *args, **kargs) -> None:
        show_me_in_city_channel = getattr(self, 'show_me_in_city_channel', None)
        picture_cost = getattr(self, 'picture_cost', None)
        video_cost = getattr(self, 'video_cost', None)
        
        # TODOlx 这两段try好像没必要了, 记得是360做兼容性加的.
        try:
            video_cost_index = int(getattr(self, 'video_cost_index', None))
        except Exception:
            video_cost_index = None
        try:
            picture_cost_index = int(getattr(self, 'picture_cost_index', None))
        except Exception:
            picture_cost_index = getattr(self, 'picture_cost_index', None)
        
        # TODOlx 驼峰下划线相互转
        data = {
            'uid': self.uid,
            'syncWeiboWithWatermark': getattr(self, 'sync_weibo_with_watermark', None),
            'showMeInCityChannel': show_me_in_city_channel,
            'pictureCost': picture_cost,
            'pictureCostIndex': picture_cost_index,
            'defaultRecommendPosition': getattr(self, 'default_recommend_position', None),
            'background': getattr(self, 'background', None),
            'showF10': getattr(self, 'show_f10', None),
            'autoFollowTopicWhenPublish': getattr(self, 'auto_follow_topic_when_publish', None),
            'showF12': getattr(self, 'show_f12', None),
            'videoCost': video_cost,
            'videoCostIndex': video_cost_index,
            'allowStrangerIm': getattr(self, 'allow_stranger_im', None),
            'foldStrangerIm': getattr(self, 'fold_stranger_im', None),
            'operatorPush': getattr(self, 'operator_push', None),
        }
        request.post(None, data)
        # ---------------------------- Side Effects START TODOlx 优雅地处理副作用, option? ----------------------------
        if show_me_in_city_channel is not None:
            try:
                # 用户同城流隐私设置
                redis_topic.lpush('nearby:user:switch', json.dumps({'uid': self.uid, 'state': show_me_in_city_channel}))
            except Exception:
                exception_logger.exception('[REDIS_TOPIC_FAIL]')

        if picture_cost is not None:  # 用户主动设置图片水滴付费下载
            if picture_cost < 0:
                download_type = 1
                price = 0
            else:
                download_type = 3
                price = picture_cost / 100  # out
            picture_download_logger.info("time:%s;uid:%s;download_type:%s;price:%s:type:download_image", int(time()), self.uid, download_type, price)
        
        if video_cost is not None:  # 用户主动设置视频水滴付费下载
            if video_cost < 0:
                download_type = 1
                price = 0
            else:
                download_type = 3
                price = video_cost / 100  # out
            picture_download_logger.info("time:%s;uid:%s;download_type:%s;price:%s:type:download_video", int(time()), self.uid, download_type, price)
        # ---------------------------- Side Effects END ----------------------------
