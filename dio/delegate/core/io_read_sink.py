from typing import Type
from .io_source import IoSource
from ...schemable.typing import Schemable
from ...share.entity import Entity


IoReadSink = None


class IoReadSink:
    """
    TLDR
        吃的是草(unknown), 挤的是奶(content)
    """
    # ---------------------------- 字段定义 START ----------------------------
    source: IoSource  # 牛
    unknown: any  # 草
    schemable_clz: Type[Schemable]  # 挤奶工具
    # ---------------------------- 字段定义 END ----------------------------
    
    def __init__(self, schemable_clz: Type[Schemable], source: IoSource, unknown: any) -> None:
        self.schemable_clz = schemable_clz
        self.unknown = unknown
        self.source = source

    @property
    def content(self) -> Entity:
        if self.schemable_clz is not None and self.source is not None:
            return self.source.content(self.schemable_clz, self.unknown)
        else:
            return self.unknown
