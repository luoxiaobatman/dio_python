from dio import compile_schema

_SCHEMA_MEDIA_FILTER_STICKER_MAPPING = {
    'id': 'sticker_id',
    'end_time': 'end_time',
    'start_time': 'start_time',
    'rank': 'rank',
}
SCHEMA_MEDIA_FILTER_STICKER_MAPPING = compile_schema(_SCHEMA_MEDIA_FILTER_STICKER_MAPPING)


_SCHEMA_MEDIA_FILTER_STICKER_CATEGORY = {
    'id': 'id',
    'platform': 'platform',
    'name': 'title',
    'rank': 'rank',
    'end_time': 'end_time',
    'start_time': 'start_time',
    'minimum_version': 'minimum_version',
    'maximum_version': 'maximum_version',
    'type': 'type',
    'sticker_mappings': ('sticker_mappings', [], SCHEMA_MEDIA_FILTER_STICKER_MAPPING),
}
SCHEMA_MEDIA_FILTER_STICKER_CATEGORY = compile_schema(_SCHEMA_MEDIA_FILTER_STICKER_CATEGORY)
