from urllib.parse import quote
from dio import compile_schema
from api_base.util.common_util import gen_url

_SCHEMA_POPUP_2021_CSK = {
    # 'id': 'adid',
    'link': (
        'scheme',
        'sinaweibo://',
        lambda x: 'sinaweibo://browser?url={}'.format(quote('https://m.weibo.cn/c/wbox?' + x[17:], safe='')) if x.startswith('sinaweibo://wbox?') else 'sinaweibo://',
        [(Exception, 'sinaweibo://')],
    ),
    'link_type': (
        '_',
        None,
        lambda _: 'schema',
    ),
    'image_url': (
        '_',
        None,
        lambda _: 'https://lz.sinaimg.cn/large/ed430cbbly3gmtxnr57haj20nc0uugpo.jpg',
    ),
    'duration': (
        '_',
        None,
        lambda _: None,
    ),
    'priority': (
        '_',
        None,
        lambda _: 3,
    ),
}

_SCHEMA_POPUP = {
    'id': 'id',
    'link': 'schema',
    'duration': 'duration',
    'image_url': ('picture_pid', None, lambda x: gen_url(x), [(Exception, None)]),
    'start_time': 'start_time',
    'end_time': 'end_time',
    'platform': 'platform',
    'rank': 'rank'
}

SCHEMA_POPUP = compile_schema(_SCHEMA_POPUP)

SCHEMA_POPUP_2021_CSK = compile_schema(_SCHEMA_POPUP_2021_CSK)
