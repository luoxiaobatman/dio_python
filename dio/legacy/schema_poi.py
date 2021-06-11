import re
from dio import compile_schema

_POSITION_PATTERN = re.compile('''^(?P<lat>-?\d+\.?\d*)(?P<lon>(\s|-|(\s-))\d+\.?\d*)$''')


SCHEMA_POI = compile_schema({
    'title': (
        [('object', 'object', 'display_name')],
        [None],
    ),
    'address': (
        [('object', 'object', 'address', 'street_address')],
        [None],
    ),
    'lat': (
        [('object', 'object', 'position')],
        [None],
        lambda x: float(re.match(_POSITION_PATTERN, x.rstrip().lstrip()).group('lat')),
    ),
    'lon': (
        [('object', 'object', 'position')],
        [None],
        lambda x: float(re.match(_POSITION_PATTERN, x.rstrip().lstrip()).group('lon')),
    )
})
