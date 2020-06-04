import asyncio
import asyncio.protocols
from codecs import CodecInfo
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    NewType,
    Optional,
    Set,
    Tuple,
    TypeVar,
    Union,
    overload,
)
from typing_extensions import Literal

import asyncpg.pgproto.pgproto

from ..connect_utils import _ConnectionParameters
from ..pgproto.pgproto import WriteBuffer
from ..types import Attribute, Type

_NoTimeoutType = NewType('_NoTimeoutType', object)
_TimeoutType = Union[float, None, _NoTimeoutType]

BUILTIN_TYPE_NAME_MAP: Dict[str, int]
BUILTIN_TYPE_OID_MAP: Dict[int, str]
NO_TIMEOUT: _NoTimeoutType

def hashlib_md5(*args: Any, **kwargs: Any) -> Any: ...

class BaseProtocol(CoreProtocol):
    queries_count: Any = ...
    __pyx_vtable__: Any = ...
    def __init__(
        self,
        addr: Any,
        connected_fut: Any,
        con_params: _ConnectionParameters,
        loop: Any,
    ) -> None: ...
    def abort(self) -> None: ...
    async def bind(
        self,
        state: PreparedStatementState,
        args: Any,
        portal_name: str,
        timeout: _TimeoutType,
    ) -> Any: ...
    @overload
    async def bind_execute(
        self,
        state: PreparedStatementState,
        args: Any,
        portal_name: str,
        limit: int,
        return_extra: Literal[False],
        timeout: _TimeoutType,
    ) -> List[Record]: ...
    @overload
    async def bind_execute(
        self,
        state: PreparedStatementState,
        args: Any,
        portal_name: str,
        limit: int,
        return_extra: Literal[True],
        timeout: _TimeoutType,
    ) -> Tuple[List[Record], bytes, bool]: ...
    @overload
    async def bind_execute(
        self,
        state: PreparedStatementState,
        args: Any,
        portal_name: str,
        limit: int,
        return_extra: bool,
        timeout: _TimeoutType,
    ) -> Union[List[Record], Tuple[List[Record], bytes, bool]]: ...
    async def bind_execute_many(
        self,
        state: PreparedStatementState,
        args: Any,
        portal_name: str,
        timeout: _TimeoutType,
    ) -> None: ...
    async def close(self, timeout: _TimeoutType) -> None: ...
    def _get_timeout(self, timeout: _TimeoutType) -> Optional[float]: ...
    def _is_cancelling(self) -> bool: ...
    async def _wait_for_cancellation(self) -> None: ...
    async def close_statement(
        self, state: PreparedStatementState, timeout: _TimeoutType
    ) -> Any: ...
    async def copy_in(self, *args: Any, **kwargs: Any) -> str: ...
    async def copy_out(self, *args: Any, **kwargs: Any) -> str: ...
    async def execute(self, *args: Any, **kwargs: Any) -> Any: ...
    def get_server_pid(self, *args: Any, **kwargs: Any) -> int: ...
    def get_settings(self, *args: Any, **kwargs: Any) -> ConnectionSettings: ...
    def is_closed(self, *args: Any, **kwargs: Any) -> Any: ...
    def is_connected(self, *args: Any, **kwargs: Any) -> Any: ...
    def is_in_transaction(self, *args: Any, **kwargs: Any) -> bool: ...
    def data_received(self, data: Any) -> None: ...
    def connection_made(self, transport: Any) -> None: ...
    def connection_lost(self, exc: Optional[Exception]) -> None: ...
    def pause_writing(self, *args: Any, **kwargs: Any) -> Any: ...
    async def prepare(self, *args: Any, **kwargs: Any) -> PreparedStatementState: ...
    async def query(self, *args: Any, **kwargs: Any) -> str: ...
    def resume_writing(self, *args: Any, **kwargs: Any) -> Any: ...
    def set_connection(self, *args: Any, **kwargs: Any) -> Any: ...
    def __reduce__(self) -> Any: ...

class Codec:
    __pyx_vtable__: Any = ...
    def __init__(
        self,
        name: str,
        schema: str,
        kind: str,
        type: int,
        format: int,
        xformat: int,
        c_encoder: Any,
    ) -> None: ...
    def __reduce__(self) -> Any: ...

class ConnectionSettings(asyncpg.pgproto.pgproto.CodecContext):
    __pyx_vtable__: Any = ...
    def __init__(self, conn_key: Any) -> None: ...
    def add_python_codec(
        self,
        typeoid: int,
        typename: str,
        typeschema: str,
        typekind: str,
        encoder: Callable[[Any], Any],
        decoder: Callable[[Any], Any],
        format: Any,
    ) -> Any: ...
    def clear_type_cache(self) -> None: ...
    def get_data_codec(self, oid: int, format: Any = ...) -> Any: ...
    def get_text_codec(self) -> CodecInfo: ...
    def register_data_types(self, types: Iterable[Any]) -> None: ...
    def remove_python_codec(
        self, typeoid: int, typename: str, typeschema: str
    ) -> None: ...
    def set_builtin_type_codec(
        self,
        typeoid: int,
        typename: str,
        typeschema: str,
        typekind: str,
        alias_to: str,
        format: Any = ...,
    ) -> Any: ...
    def __getattr__(self, name: str) -> Any: ...
    def __reduce__(self) -> Any: ...

class CoreProtocol:
    backend_pid: Any = ...
    backend_secret: Any = ...
    __pyx_vtable__: Any = ...
    def __init__(self, con_params: _ConnectionParameters) -> None: ...

class DataCodecConfig:
    __pyx_vtable__: Any = ...
    def __init__(self, cache_key: Any) -> None: ...
    def add_python_codec(
        self,
        typeoid: int,
        typename: str,
        typeschema: str,
        typekind: str,
        encoder: Callable[[ConnectionSettings, WriteBuffer, object], object],
        decoder: Callable[..., object],
        format: Any,
        xformat: Any,
    ) -> Any: ...
    def add_types(self, types: Iterable[Any]) -> Any: ...
    def clear_type_cache(self) -> None: ...
    def declare_fallback_codec(self, oid: int, name: str, schema: str) -> Codec: ...
    def remove_python_codec(
        self, typeoid: int, typename: str, typeschema: str
    ) -> Any: ...
    def set_builtin_type_codec(
        self,
        typeoid: int,
        typename: str,
        typeschema: str,
        typekind: str,
        alias_to: str,
        format: Any = ...,
    ) -> Any: ...
    def __reduce__(self) -> Any: ...

class PreparedStatementState:
    closed: bool = ...
    name: str = ...
    query: str = ...
    refs: int = ...
    __pyx_vtable__: Any = ...
    def __init__(self, name: str, query: str, protocol: BaseProtocol) -> None: ...
    def _get_parameters(self) -> Tuple[Type, ...]: ...
    def _get_attributes(self) -> Tuple[Attribute, ...]: ...
    def _init_types(self) -> Set[int]: ...
    def _init_codecs(self) -> None: ...
    def attach(self) -> None: ...
    def detach(self) -> None: ...
    def mark_closed(self) -> None: ...
    def __reduce__(self) -> Any: ...

class Protocol(BaseProtocol, asyncio.protocols.Protocol): ...

_T = TypeVar('_T')

class Record:
    @overload
    def get(self, key: str) -> Optional[Any]: ...
    @overload
    def get(self, key: str, default: _T) -> Union[Any, _T]: ...
    def items(self) -> Iterator[Tuple[str, Any]]: ...
    def keys(self) -> Iterator[str]: ...
    def values(self) -> Iterator[Any]: ...
    @overload
    def __getitem__(self, index: str) -> Any: ...
    @overload
    def __getitem__(self, index: int) -> Any: ...
    @overload
    def __getitem__(self, index: slice) -> Tuple[Any, ...]: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __contains__(self, x: object) -> bool: ...
    def __len__(self) -> int: ...

class Timer:
    def __init__(self, budget: Optional[float]) -> None: ...
    def get_remaining_budget(self) -> float: ...
    def __enter__(self) -> None: ...
    def __exit__(self, et: Any, e: Any, tb: Any) -> None: ...
