from dio import compile_schema
from api_base.g import G
from api_base.util.date_util import parse_wb_time


SCHEMA_USER = compile_schema({
    'uid': 'id',
    'name': 'screen_name',
    'description': 'description',
    'image': 'avatar_large',
    'image_small': 'profile_image_url',
    'image_hd': 'avatar_hd',
    'city': 'location',
    'relationship': (
        ['following', 'follow_me'],
        [None, False],
        # 0 不关注 1 关注 2 我的粉丝 3 互相关注
        lambda following, follow_me: int(not not following) + 2 if follow_me and G.CTX.get_version() > '1.5.1' else int(not not following),
    ),
    'follower_count': 'followers_count',
    'following_count': 'friends_count',
    'status_count': 'statuses_count',
    'birthday': 'birthday',
    'constellation': 'constellation',
    'gender': 'gender',
    'verified_type': 'verified_type',
    'verified_reason': 'verified_reason',
    'from_spider': (
        [('extend', 'system')],
        [0],
    ),
    'create_time': (
        'created_at',
        None,
        lambda x: parse_wb_time(x),
    ),
    'special_following': 'special_following',
    'like_favorites_count': (
        ['liked_count', 'collected_count'],
        [0, 0],
        lambda x1, x2: x1 + x2,
    ),
    'accuracy_matched': (
        'accuracy_matched',
        0
    ),
})
