"""
WIKI: http://wiki.intra.sina.com.cn/pages/viewpage.action?pageId=202446170
"""
from api_base.g import G
from dio import compile_schema


SCHEMA_MESSAGE_UNREAD = compile_schema({
    'all_likes': (
        ['oasis_all_attitude', 'oasis_comment_attitude'],
        [0, 0],
        lambda x, y: max(x, 0) + (0 if G.CTX.get_version() < '2.1.0' else max(y, 0)),
        [(Exception, 0)],
    ),
    'all_comment': (
        ['oasis_all_cmt', 'oasis_rainbow_fart_cmt', 'oasis_quick_emoticon_cmt', 'oasis_all_mention_status',
         'oasis_all_mention_cmt', 'oasis_all_text_mention_status', 'oasis_all_mention_video'],
        [0]*7,
        lambda *args: sum([max(_) for _ in zip(args, [0]*7)]),
        [(Exception, 0)],
    ),
    'all_followers': (
        'oasis_all_follower',
        0,
        lambda x: max(x, 0),
        [(Exception, 0)],
    ),
    'all_common_guide_attention': (
        'oasis_all_common_guide_attention',
        0,
        lambda x: max(x, 0),
        [(Exception, 0)],
    ),
    'unread_statuses': (
        'oasis_unread',
        0,
        lambda x: max(x, 0),
        [(Exception, 0)],
    ),
    'new_statuses': (
        'oasis_pageup_unread',
        0,
        lambda x: max(x, 0),
        [(Exception, 0)],
    ),
    'all_cmt': (
        ['oasis_all_cmt', 'oasis_rainbow_fart_cmt', 'oasis_quick_emoticon_cmt'],
        [0, 0, 0],
        lambda *args: sum([max(_) for _ in zip(args, [0, 0, 0])]),
        [(Exception, 0)],
    ),
    'rainbow_fart_cmt': (
        'oasis_rainbow_fart_cmt',
        0,
        lambda x: max(x, 0),
        [(Exception, 0)],
    ),
    'quick_emoticon_cmt': (
        'oasis_quick_emoticon_cmt',
        0,
        lambda x: max(x, 0),
        [(Exception, 0)],
    ),
    'attention_cmt': (
        'oasis_attention_cmt',
        0,
        lambda x: max(x, 0),
        [(Exception, 0)],
    ),
    'oasis_all_cmt': (
        'oasis_all_cmt',
        0,
        lambda x: max(x, 0),
        [(Exception, 0)],
    ),
    'all_at': (
        ['oasis_all_mention_status', 'oasis_all_mention_cmt', 'oasis_all_text_mention_status', 'oasis_all_mention_video'],
        [0]*4,
        lambda *args: sum([max(_) for _ in zip(args, [0]*4)]),
        [(Exception, 0)],
    ),
    'attention_at': (
        ['oasis_attention_mention_status', 'oasis_attention_mention_cmt', 'oasis_attention_text_mention_status', 'oasis_attention_mention_video'],
        [0]*4,
        lambda *args: sum([max(_) for _ in zip(args, [0]*4)]),
        [(Exception, 0)],
    ),
    'oasis_new_rainbow_fart': (
        'oasis_new_rainbow_fart',
        0,
        lambda x: max(x, 0),
        [(Exception, 0)],
    ),
    'oasis_paper_plane': (
        'oasis_paper_plane',
        0,
        lambda x: max(x, 0),
        [(Exception, 0)],
    ),
    'oasis_microphone': (
        'oasis_microphone',
        0,
        lambda x: max(x, 0),
        [(Exception, 0)],
    ),
    'oasis_praise_all': (
        ['oasis_new_rainbow_fart', 'oasis_paper_plane', 'oasis_microphone'],
        [0, 0, 0],
        lambda *args: sum([max(_) for _ in zip(args, [0, 0, 0])]),
        [(Exception, 0)],
    ),
})
