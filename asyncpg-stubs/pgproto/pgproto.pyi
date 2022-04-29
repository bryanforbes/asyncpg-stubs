import uuid
from codecs import CodecInfo
from typing import AnyStr
from typing_extensions import final

class CodecContext:
    def get_text_codec(self) -> CodecInfo: ...

@final
class ReadBuffer: ...

@final
class WriteBuffer: ...

class BufferError(Exception): ...

@final
class UUID(uuid.UUID):
    def __init__(self, inp: AnyStr) -> None: ...
