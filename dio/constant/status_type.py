from enum import Enum


class StatusTypeDef(Enum):
    type_image = 1
    type_video = 2
    type_image_subtype_flag = 3  # V3.6.5打卡动态
    type_image_subtype_moment = 4  # V3.6.5此刻动态
