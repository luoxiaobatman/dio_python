from dio import compile_schema

_SCHEMA_PAYMENT_HISTORY = {
    'id': 'sticker_id',
    'end_time': 'end_time',
    'start_time': 'start_time',
}
SCHEMA_CONTENT_PAYMENT_PAYMENT_HISTORY = compile_schema(_SCHEMA_PAYMENT_HISTORY)


_SCHEMA_PAYMENT_HISTORY_NEXTABLE = {
    'next_cursor': 'next_cursor',
    'list': ('list', None, ),
}
SCHEMA_CONTENT_PAYMENT_PAYMENT_HISTORY_NEXTABLE = compile_schema(_SCHEMA_PAYMENT_HISTORY_NEXTABLE)
