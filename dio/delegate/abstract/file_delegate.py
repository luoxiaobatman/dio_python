"""
通常意义下的文件, 而非unix的一切皆file的file
"""
from abc import abstractmethod
from io import TextIOWrapper
from typing import TypeVar, Type, Generic
from ..core.option_http import OptionHttp
from ..typing import IoDelegate


T = TypeVar('T', bound=IoDelegate)
E = TypeVar('E')
RO = TypeVar('RO', bound=OptionHttp)
WO = TypeVar('WO', bound=OptionHttp)


class FileDelegate(IoDelegate[E, RO, WO], Generic[E, RO, WO]):
    """
    TODOlx
    本地文件, 即在block device的file
    """
    Entity: Type[E] = None
    ReadOption: Type[RO] = None
    WriteOption: Type[WO] = None

    def read(self: T, option: RO) -> E:
        raise NotImplementedError

    def write(self: T, option: WO) -> any:
        raise NotImplementedError

    def _post_read(self: T, entity: E, option: RO) -> E:
        return entity

    @abstractmethod
    def _do_write(self: T, file: TextIOWrapper, option: WO) -> any:
        raise NotImplementedError

    @abstractmethod
    def _do_read(self: T, file: TextIOWrapper, option: RO) -> any:
        raise NotImplementedError
