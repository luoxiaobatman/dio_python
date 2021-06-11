from typing import List, Dict, Optional
from dio.share.entity import Entity


class EntityContentPaymentHistory(Entity):
    cuid: int  # 付款方
    ouid: int  # 收款方(博主)
    download_time: int  # 下载时间
    order_id: str  # 水滴订单id
    cost: int  # 支付水滴金额
    sid: int
    pid: str


class EntityContentPaymentHistoryListable(Entity):
    uid: int  # 博主
    sid: Optional[int]  # 博主动态
    pid: Optional[int]  # 动态下的某张图片
    summary: Dict[str, int]  # {pid: count}
    list: List[EntityContentPaymentHistory]
    next_cursor: str
    cursor: Optional[str]
    count: Optional[int]


class EntityContentDownloadHistoryListable(Entity):
    uid: int  # 付费者
    list: List[EntityContentPaymentHistory]
    next_cursor: str
    cursor: Optional[str]
    count: Optional[int]
