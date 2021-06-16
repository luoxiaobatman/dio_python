# from abc import abstractmethod
# import sys
# from redis import Redis
# from typing import Optional, TextIO, TypeVar, Type, Generic
# from ..core.io_read_sink import IoReadSink
# from ..core.option_base import OptionBase
# from ..core.io_source import IoSourceStd
# from ..typing import IoDelegate
# from ...share.entity import Entity


# T = TypeVar('T', bound=IoDelegate)
# E = TypeVar('E', bound=Entity)


# io_source_std = IoSourceStd("")  # TODO


# class ReadOption(OptionBase):
#     def __init__(self):
#         super().__init__(source=io_source_std)


# class WriteOption(OptionBase):
#     def __init__(self, _v365: bool):
#         super().__init__(source=io_source_std)


# class StdData(Entity):
#     text: str
    

# # class HttpDelegate(IoDelegate[E, RO, WO], Generic[E, RO, WO]):

# class StdioDelegate(StdData, IoDelegate[StdData, ReadOption, WriteOption]):
#     stdin: TextIO
#     stdout: TextIO
#     stderr: TextIO
    
#     def __init__(self, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr) -> None:
#         self.stdin = stdin
#         self.stdout = stdout
#         self.stderr = stderr

#     Entity = StdData
#     ReadOption = ReadOption
#     WriteOption = WriteOption
    
#     def read(self, option: ReadOption) -> Optional[StdData]:
#         raise NotImplementedError
        
#     def write(self, option: WriteOption):
#         self.stdout.write('foobar')
#         self.stdout.flush()
#         # self._do_write(option._redis_.client, option)


# def pipe(UsingDelegateReadPoint, UsingDeletateWritePoint) -> Type[IoDelegate]:
#     """
#     """
    
#     pass

# # read write
# # pipe: a method of overwriting source
# # A.read -> read ->
# # delegate_a
# # delegate_b
# # 假如不是同一个entity, 不能pipe
# # delegate_c = pipable.pipe(delegate_a, dlegate_d)
# # delegate_c.read()
# # delegate_c.write()

# # delegate_c.pipe(delegate_f)
# # pipe(delegate_a, dlegate_d)
