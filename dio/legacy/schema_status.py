from time import time
from api_base.g import G
from api_base.util.date_util import parse_wb_time
from api_base.util.constant import StatusConstant
from dio import compile_schema
from .schema_poi import SCHEMA_POI
from .schema_user import SCHEMA_USER


"""

                        .type dep   ┌────────┐    dep
                 ┌─────────────────<┤ status ├>───────────────────────────────────────────────┐
                 │                  └────┬───┘                                                │
                 │                       │                                                    │
     ┌───────────┼───────────────┬───────┴──────────────────────────────────┬─────────────────┼─────────────┐
     │           │               │                                          │                 │             │
  ┌──┴───┐       │        ┌──────┴──────┐         mutual dep         ┌──────┴────────┐        │     ┌───────┴───────┐
  │ user │       └───────>┤ List[media] ├<──────────────────────────>┤ dynamic_cover ├<───────┘     │ advertisement │
  └──────┘                └──────┬──────┘                            └───────────────┘              └───────────────┘
                                 │
                        ┌────────┴─────────┐
                        │ List[annotation] │
                        └────────┬─────────┘
                                 │
                    ┌────────────┼──────────┐
                    │            │          │
                ┌───┴───┐    ┌───┴──┐    ┌──┴──┐
                │ brand │    │ user │    │ poi │
                └───────┘    └──────┘    └─────┘

"""


def _status_extra(status_map_annotations):
    if not isinstance(status_map_annotations, list):
        return None
    for extra in status_map_annotations:
        if G.S.safe_dict_get(extra, 'oasis') == 1:
            return extra
    return None


_SCHEMA_STATUS_ANNOTATION_BRAND = {
    'id': 'id',
    'name': 'name',
    'image': 'image',
}
SCHEMA_STATUS_ANNOTATION_BRAND = compile_schema(_SCHEMA_STATUS_ANNOTATION_BRAND)

_SCHEMA_STATUS_ANNOTATION = {
    'type': 'type',
    'direction': 'direction',
    'left': 'left',
    'top': 'top',
    'bid': 'bid',
    'uid': 'uid',
    'text': 'text',
    'poiid': 'poiId',
    'name': 'name',
    'oid': 'oid',
    'brand': (
        'info',
        None,
        SCHEMA_STATUS_ANNOTATION_BRAND,
        [(Exception, None)],
        lambda from_dict: G.S.safe_dict_get(from_dict, 'type') == 1,
    ),
    'user': (
        'info',
        None,
        SCHEMA_USER,
        [(Exception, None)],
        lambda from_dict: G.S.safe_dict_get(from_dict, 'type') == 2,
    ),
    'poi': (
        'info',
        None,
        SCHEMA_POI,
        [(Exception, None)],
        lambda from_dict: G.S.safe_dict_get(from_dict, 'type') == 3,
    ),
}
SCHEMA_STATUS_ANNOTATION = compile_schema(_SCHEMA_STATUS_ANNOTATION)


_SCHEMA_STATUS_MEDIA = {
    'annotations': SCHEMA_STATUS_ANNOTATION,
    'height': 'height',
    'width': 'width',
    '_pid': 'pid',
    'fid': 'fid',
    'type': 'type',
    # normal_url      在pid setter里面处理 
    # origin_url      在pid setter里面处理 
    # medium_url      在pid setter里面处理 
    # small_url       在pid setter里面处理
    # thumbnail_url   在pid setter里面处理    
}
SCHEMA_STATUS_MEDIA = compile_schema(_SCHEMA_STATUS_MEDIA)


_SCHEMA_STATUS_DYNAMIC_COVER = {
    'url': 'url',
    'width': 'width',
    'height': 'height',
}

SCHEMA_STATUS_DYNAMIC_COVER = compile_schema(_SCHEMA_STATUS_DYNAMIC_COVER)

_SCHMEA_STATUS_ADVERTISEMENT = {
    'ad_type': (
        'ad_type',
        None,
        lambda x: G.S.safe_int(x, 2),
    ),
    'schema': (
        'schema',
        '',
    ),
    'schema_title': (
        'schema_title',
        '',
    ),
    'mark': (
        'mark',
        '',
    ),
    'position': (
        'position',
        None,
        lambda x: G.S.safe_int(x),
    ),
}
SCHMEA_STATUS_ADVERTISEMENT = compile_schema(_SCHMEA_STATUS_ADVERTISEMENT)


def _convert_edit_state(createAt, canEdit, editCount):
    create_time = parse_wb_time(createAt)
    if create_time + 72 * 3600 * 1000 < int(time() * 1000):
        return StatusConstant.EDIT_TIME_LIMIT
    if canEdit:
        return StatusConstant.EDIT_ALLOW
    elif isinstance(editCount, int) and editCount >= 3:
        return StatusConstant.EDIT_COUNT_LIMIT
    else:
        return StatusConstant.EDIT_FORBIDDEN


_SCHEMA_STATUS = {
    'user': SCHEMA_USER,
    'medias': (
        'media',
        None,
        SCHEMA_STATUS_MEDIA,
    ),
    'dynamic_cover': (
        [('objects', 'dynamic_cover')],  # objects原始为数组类型, 根据绿洲规则在pre_schema里面转换成了dict类型
        [None],
        SCHEMA_STATUS_DYNAMIC_COVER,
    ),
    'poi': (
        [('objects', 'poi')],
        [None],
        SCHEMA_POI,
    ),
    'advertisement': (
        'advertisement',
        None,
        SCHMEA_STATUS_ADVERTISEMENT,
    ),
    'id': (
        'id',
        None,
        lambda x: int(x),
    ),
    'share_id': (
        'id',
        None,
        lambda x: str(x),
    ),
    'mid': (
        'cMid',
        0,
        lambda x: int(x),
    ),
    'create_time': (
        'createAt',
        None,
        parse_wb_time,
    ),
    'uid': 'uid',
    'oasis': (
        'cMid',
        None,
        lambda x: not x,
    ),
    'text': 'text',
    'recommend_reason': 'recommend_reason',
    'title': 'title',
    'comment_total': 'commentsCount',
    'like_total': 'attitudesCount',
    'is_like': 'isLiked',
    'poiid': 'poiId',
    'state': (
        ['apiState', ('context', 'strictOp')],
        [None, None],
        lambda apiState, strictOp: StatusConstant.VISIBLE_SHIELD if strictOp == 1 else apiState,  # strictOp 现在可见性0, 监控删除返回1
    ),
    'extra': (
        'annotations',
        None,
        _status_extra,
    ),
    'can_edit': (
        [('context', 'canEdit')],
        [False],
        lambda x: bool(x),
    ),
    'edit_state': (
        ['createAt', ('context', 'canEdit'), 'editCount'],
        [None, None, None],
        _convert_edit_state,
    ),
    'show_tree_comment': (
        'showTreeComment',
        'None',
        lambda x: not not x,  # bool(x) ???
    ),
    'show_hot_comment': (
        [('context', 'showHotComment')],
        [None],
        lambda x: not not x,
    ),
    'is_favorited': (
        [('context', 'isFavorited')],
        [None],
    ),
    'score': (
        [('context', 'score')],
        [None],
    ),
}
SCHEMA_STATUS = compile_schema(_SCHEMA_STATUS)
