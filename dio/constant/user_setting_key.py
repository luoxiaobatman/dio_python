from enum import Enum
from typing import List
from dio.mixin.immutable import Immutable


UserSettingKeyDescriptor = None


class UserSettingKeyValueDef(Enum):
    """
    TODOlx, 继承EnumMeta, 重写方法
    enum.EnumMeta
    enum的value具有唯一性
    value compare用"=="表达式
    """
    sync_weibo_with_watermark_sync = 1
    sync_weibo_with_watermark_nosync = 0
    show_me_in_city_channel_show = 1
    show_me_in_city_channel_noshow = 0
    picture_cost_forbidden = -1
    picture_cost_index_forbidden = -1
    video_cost_forbidden = -2
    video_cost_index_forbidden = -2
    cost_masked = -3  # 装作不知道
    cost_index_masked = -3  # 装作不知道
    default_recommend_position_default = 1
    background_default = 'ed430cbbly3gfn5a0ze08j20v90higsm'
    background_url_default = 'https://lz.sinaimg.cn/large/ed430cbbly3gfn5a0ze08j20v90higsm.jpg'
    available_picture_costs_default = [2, 200, 10000, 20000]  # TODOlx 应用global_config的default
    available_video_costs_default = [2, 200, 10000, 20000]  # TODOlx 应用global_config的default
    show_f10_show = 1
    show_f10_hide = 0
    show_f12_show = 1
    show_f12_hide = 0
    auto_follow_topic_when_publish_publish = 1
    auto_follow_topic_when_publish_noop = 0
    video_forbidden_true = True
    video_forbidden_false = False
    picture_forbidden_true = True
    picture_forbidden_false = False
    allow_stranger_im_allow = 1
    allow_stranger_im_noallow = 0
    fold_stranger_im_fold = 1
    fold_stranger_im_expand = 0
    operator_push_yes = 1
    operator_push_no = 0


class UserSettingKeyDescriptor(Immutable):
    @property
    def serialized(self) -> str:
        return tuple.__getitem__(self, 0)
    @property
    def default(self) -> UserSettingKeyValueDef:
        return tuple.__getitem__(self, 1)
    @property
    def standalone(self) -> bool:
        return tuple.__getitem__(self, 2)
    @property
    def depends(self) -> List[UserSettingKeyDescriptor]:
        return tuple.__getitem__(self, 3)

    def __init__(self, serialized, default: UserSettingKeyValueDef, standalone: bool, depends: List[UserSettingKeyDescriptor]):
        pass


# KD is key descriptor
KD_sync_weibo_with_watermark = UserSettingKeyDescriptor('sync_weibo_with_watermark', UserSettingKeyValueDef.sync_weibo_with_watermark_sync, True, None)
KD_show_me_in_city_channel = UserSettingKeyDescriptor('show_me_in_city_channel', UserSettingKeyValueDef.show_me_in_city_channel_show, True, None)
KD_picture_cost_index = UserSettingKeyDescriptor('picture_cost_index', UserSettingKeyValueDef.picture_cost_index_forbidden, True, None)
KD_picture_cost = UserSettingKeyDescriptor('picture_cost', UserSettingKeyValueDef.picture_cost_forbidden, False, [KD_picture_cost_index])
KD_video_cost_index = UserSettingKeyDescriptor('video_cost_index', UserSettingKeyValueDef.video_cost_index_forbidden, True, None)
KD_video_cost = UserSettingKeyDescriptor('video_cost', UserSettingKeyValueDef.video_cost_forbidden, False, [KD_video_cost_index])
KD_default_recommend_position = UserSettingKeyDescriptor('default_recommend_position', UserSettingKeyValueDef.default_recommend_position_default, True, None)
KD_background = UserSettingKeyDescriptor('background', UserSettingKeyValueDef.background_default, True, None)
KD_background_url = UserSettingKeyDescriptor('background_url', UserSettingKeyValueDef.background_url_default, False, [KD_background])
KD_available_picture_costs = UserSettingKeyDescriptor('available_picture_costs', UserSettingKeyValueDef.available_picture_costs_default, False, [KD_picture_cost, KD_picture_cost_index])
KD_available_video_costs = UserSettingKeyDescriptor('available_video_costs', UserSettingKeyValueDef.available_video_costs_default, False, [KD_video_cost, KD_video_cost_index])
KD_auto_follow_topic_when_publish = UserSettingKeyDescriptor('auto_follow_topic_when_publish', UserSettingKeyValueDef.auto_follow_topic_when_publish_publish, True, None)
KD_show_f10 = UserSettingKeyDescriptor('show_f10', UserSettingKeyValueDef.show_f10_show, True, None)
KD_show_f12 = UserSettingKeyDescriptor('show_f12', UserSettingKeyValueDef.show_f12_show, True, None)
KD_video_forbidden = UserSettingKeyDescriptor('video_forbidden', UserSettingKeyValueDef.video_forbidden_true, False, [KD_video_cost])
KD_picture_forbidden = UserSettingKeyDescriptor('picture_forbidden', UserSettingKeyValueDef.picture_forbidden_true, False, [KD_picture_cost])
KD_allow_stranger_im = UserSettingKeyDescriptor('allow_stranger_im', UserSettingKeyValueDef.allow_stranger_im_allow, True, None)
KD_fold_stranger_im = UserSettingKeyDescriptor('fold_stranger_im', UserSettingKeyValueDef.fold_stranger_im_fold, True, None)
KD_operator_push = UserSettingKeyDescriptor('operator_push', UserSettingKeyValueDef.operator_push_yes, True, None)


class UserSettingKey:
    sync_weibo_with_watermark = KD_sync_weibo_with_watermark
    show_me_in_city_channel = KD_show_me_in_city_channel
    picture_cost = KD_picture_cost
    picture_cost_index = KD_picture_cost_index
    video_cost = KD_video_cost
    video_cost_index = KD_video_cost_index
    default_recommend_position = KD_default_recommend_position
    background = KD_background
    background_url = KD_background_url
    available_picture_costs = KD_available_picture_costs
    available_video_costs = KD_available_video_costs
    auto_follow_topic_when_publish = KD_auto_follow_topic_when_publish
    show_f10 = KD_show_f10
    show_f12 = KD_show_f12
    video_forbidden = KD_video_forbidden
    picture_forbidden = KD_picture_forbidden
    allow_stranger_im = KD_allow_stranger_im
    fold_stranger_im = KD_fold_stranger_im
    operator_push = KD_operator_push
    @staticmethod
    def read_keys() -> List[UserSettingKeyDescriptor]:
        return [UserSettingKey.picture_cost,
                UserSettingKey.video_cost,
                UserSettingKey.sync_weibo_with_watermark,
                UserSettingKey.available_picture_costs,
                UserSettingKey.available_video_costs,
                UserSettingKey.default_recommend_position,
                UserSettingKey.auto_follow_topic_when_publish,
                UserSettingKey.show_f10,
                UserSettingKey.show_f12,
                UserSettingKey.allow_stranger_im,
                UserSettingKey.fold_stranger_im,
                UserSettingKey.operator_push,
                UserSettingKey.background_url,
                UserSettingKey.show_me_in_city_channel]

    @staticmethod
    def write_keys() -> List[UserSettingKeyDescriptor]:
        return [UserSettingKey.sync_weibo_with_watermark,
                UserSettingKey.picture_cost,
                UserSettingKey.show_me_in_city_channel,
                UserSettingKey.video_cost,
                UserSettingKey.default_recommend_position,
                UserSettingKey.background,
                UserSettingKey.show_f10,
                UserSettingKey.auto_follow_topic_when_publish,
                UserSettingKey.show_f12,
                UserSettingKey.allow_stranger_im,
                UserSettingKey.fold_stranger_im,
                UserSettingKey.operator_push]

    @staticmethod
    def pre_200_keys() -> List[UserSettingKeyDescriptor]:
        return [UserSettingKey.show_me_in_city_channel, UserSettingKey.sync_weibo_with_watermark, UserSettingKey.picture_cost, UserSettingKey.default_recommend_position]
