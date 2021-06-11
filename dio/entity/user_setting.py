from typing import List

from dio.share.entity import Entity

from api_base.util.mixin import MixinResponsePostProcessor
from api_base.exception import ToastException

from ..constant import UserSettingKey as K, UserSettingKeyValueDef as D


class EntityUserSetting(Entity, MixinResponsePostProcessor):
    # ---------------------------- Base 字段定义 START ----------------------------
    uid: int
    sync_weibo_with_watermark: int
    show_me_in_city_channel: int
    picture_cost: int
    picture_cost_index: int
    video_cost: int
    video_cost_index: int
    default_recommend_position: int
    background: int
    background_url: str
    available_picture_costs: List[float]
    available_video_costs: List[float]
    auto_follow_topic_when_publish: int
    picture_forbidden: bool
    video_forbidden: bool
    show_f10: int
    show_f12: int
    allow_stranger_im: int
    operator_push: int
    # ---------------------------- Base 字段定义 END ----------------------------

    CACHE_FIELDS = ['uid', 'picture_cost_index', 'video_cost_index', 'picture_forbidden', 'video_forbidden']
    
    def populate_kv(self, keys: List[D], values: str, available_picture_costs: List[int], available_video_costs: List[int]) -> None:
        """
        客户端传值keys,values. 反序列化成对象
        TODO 更优雅的反序列化
        """
        for k, v in zip(keys, values):
            if k == K.picture_cost:
                costs = available_picture_costs
                cost = _video_cost_or_picture_cost_convert(v)
                forbiden_value = D.picture_cost_forbidden.value
                if cost != forbiden_value and cost not in costs:
                    raise ToastException('无此水滴选项')
                    # return Response.custom_fail('无此水滴选项').result()
                self.picture_cost_index = costs.index(cost) if cost != forbiden_value else D.picture_cost_index_forbidden.value
                self.picture_cost = cost
            elif k == K.video_cost:
                costs = available_video_costs
                cost = _video_cost_or_picture_cost_convert(v)
                forbiden_value = D.video_cost_forbidden.value
                if cost == -1:  # 客户端用-1表示禁止
                    cost = D.video_cost_index_forbidden.value  # 应用程序用-2表示禁止
                if cost != forbiden_value and cost not in costs:
                    raise ToastException('无此水滴选项')
                self.video_cost_index = costs.index(cost) if cost != forbiden_value else D.video_cost_index_forbidden.value
                self.video_cost = cost
            elif k == K.background:
                self.background = v
            else:
                setattr(self, k.serialized, int(bool(int(v))))
    
    def _do_post_process_response(self, **kargs):
        """
        客户端
            cost是浮点数
            video_cost用-1表示禁止
        """
        if getattr(self, K.video_cost.serialized, None) is not None:
            if self.video_cost >= 0:
                cs = self.available_video_costs
                c = self.video_cost
                i = self.video_cost_index
                if len(cs) > i:
                    cs[i] = c  # 产品需求 之 档位覆盖
                self.video_cost = c / 100  # 客户端需要浮点数
            elif self.video_cost == D.video_cost_index_forbidden.value:
                self.video_cost = -1  # 客户端-1禁止, 应用程序-2禁止
                self.video_cost_index = -1  # 客户端-1禁止, 应用程序-2禁止
            else:
                self.video_cost = None
                self.video_cost_index = None
        if getattr(self, 'picture_cost', None) is not None:
            if self.picture_cost >= 0:
                cs = self.available_picture_costs
                c = self.picture_cost
                i = self.picture_cost_index
                if len(cs) > i:
                    cs[i] = c  # 产品需求 之 档位覆盖
                self.picture_cost = c / 100  # 客户端需要浮点数
        
        # 客户端需要浮点数
        if getattr(self, 'available_video_costs', None) is not None:
            self.available_video_costs = [cost / 100 for cost in self.available_video_costs]
        # 客户端需要浮点数
        if getattr(self, 'available_picture_costs', None) is not None:
            self.available_picture_costs = [cost / 100 for cost in self.available_picture_costs]


def _video_cost_or_picture_cost_convert(v: str) -> int:
    f = float(v)
    if f > 0:
        return int(f * 100)
    else:
        return int(f)
