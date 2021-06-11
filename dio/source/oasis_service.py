from typing import Type
from dio import Schemable, IoSource, Entity
from api_base.settings import config


class IoSourceOasisService(IoSource):
    def content(self, schemable_clz: Type[Schemable], data: dict) -> Entity:
        return schemable_clz.from_dict(data)

    def __repr__(self):
        return 'IoSourceOasisService instance'


io_source_oasis_service = IoSourceOasisService(config().SERVICE_URL)
