from dio import compile_schema
from api_base.util.common_util import gen_url
from api_base.util.oasisimgbed import Unistore

_SCHEMA_MAGIC_BOARD = {
    'id': 'id',
    'name': 'magic_board_name',
    'text': 'text',
    'image_url': ('thumbnail_pid', None, lambda x: gen_url(x), [(Exception, None)]),
    'small_image_url': ('small_thumbnail_pid', None, lambda x: gen_url(x), [(Exception, None)]),
    'platform': 'platform',
    'rank': 'rank',
    'image_width': 'thumbnail_width',
    'image_height': 'thumbnail_height',
    'minimum_version': 'minimum_version',
    'maximum_version': 'maximum_version',
    'zip_url': (
        ['file_usid', 'file_md5'], [None, None], lambda file_usid, file_md5: Unistore.get_zip_url(file_usid, file_md5),
        [(Exception, None)])
}

SCHEMA_MAGIC_BOARD = compile_schema(_SCHEMA_MAGIC_BOARD)
