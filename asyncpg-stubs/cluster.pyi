from asyncio import AbstractEventLoop
from ssl import SSLContext
from typing import Any, Callable, Optional, Tuple, Type, TypeVar, Union, overload
from typing_extensions import TypedDict

from .connection import Connection
from .types import ServerVersion

class _ConnectionSpec(TypedDict):
    host: str
    port: str

def platform_exe(name: str) -> str: ...
def find_available_port(
    port_range: Tuple[int, int] = ..., max_tries: int = ...
) -> Optional[int]: ...

class ClusterError(Exception): ...

_C = TypeVar('_C', bound=Connection)

class Cluster:
    def __init__(
        self, data_dir: str, *, pg_config_path: Optional[str] = ...
    ) -> None: ...
    def get_pg_version(self) -> ServerVersion: ...
    def is_managed(self) -> bool: ...
    def get_data_dir(self) -> str: ...
    def get_status(self) -> str: ...
    @overload
    async def connect(
        self,
        loop: Optional[AbstractEventLoop] = ...,
        *,
        user: Optional[str] = ...,
        password: Optional[str] = ...,
        passfile: Optional[str] = ...,
        database: Optional[str] = ...,
        timeout: int = ...,
        statement_cache_size: int = ...,
        max_cached_statement_lifetime: int = ...,
        max_cacheable_statement_size: int = ...,
        command_timeout: Optional[int] = ...,
        ssl: Optional[Union[bool, SSLContext]] = ...,
        server_settings: Optional[Any] = ...,
    ) -> Connection: ...
    @overload
    async def connect(
        self,
        loop: Optional[AbstractEventLoop] = ...,
        *,
        user: Optional[str] = ...,
        password: Optional[str] = ...,
        passfile: Optional[str] = ...,
        database: Optional[str] = ...,
        timeout: int = ...,
        statement_cache_size: int = ...,
        max_cached_statement_lifetime: int = ...,
        max_cacheable_statement_size: int = ...,
        command_timeout: Optional[int] = ...,
        ssl: Optional[Union[bool, SSLContext]] = ...,
        connection_class: Type[_C] = ...,
        server_settings: Optional[Any] = ...,
    ) -> _C: ...
    def init(self, **settings: Any) -> str: ...
    def start(
        self, wait: int = ..., *, server_settings: Any = ..., **opts: Any
    ) -> None: ...
    def reload(self) -> None: ...
    def stop(self, wait: int = ...) -> None: ...
    def destroy(self) -> None: ...
    def get_connection_spec(self) -> _ConnectionSpec: ...
    def override_connection_spec(self, **kwargs: Any) -> None: ...
    def reset_wal(
        self, *, oid: Optional[Any] = ..., xid: Optional[Any] = ...
    ) -> None: ...
    def reset_hba(self) -> None: ...
    def add_hba_entry(
        self,
        *,
        type: str = ...,
        database: str,
        user: str,
        address: Optional[str] = ...,
        auth_method: str,
        auth_options: Optional[Any] = ...,
    ) -> None: ...
    def trust_local_connections(self) -> None: ...
    def trust_local_replication_by(self, user: str) -> None: ...

class TempCluster(Cluster):
    def __init__(
        self,
        *,
        data_dir_suffix: Optional[Any] = ...,
        data_dir_prefix: Optional[Any] = ...,
        data_dir_parent: Optional[Any] = ...,
        pg_config_path: Optional[Any] = ...,
    ) -> None: ...

class HotStandbyCluster(TempCluster):
    def __init__(
        self,
        *,
        master: Any,
        replication_user: Any,
        data_dir_suffix: Optional[Any] = ...,
        data_dir_prefix: Optional[Any] = ...,
        data_dir_parent: Optional[Any] = ...,
        pg_config_path: Optional[Any] = ...,
    ) -> None: ...
    def init(self, **settings: Any) -> str: ...

class RunningCluster(Cluster):
    conn_spec: _ConnectionSpec = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def is_managed(self) -> bool: ...
    def get_connection_spec(self) -> _ConnectionSpec: ...
    def get_status(self) -> str: ...
    def init(self, **settings: Any) -> str: ...
    def start(self, wait: int = ..., **settings: Any) -> None: ...
    def stop(self, wait: int = ...) -> None: ...
    def destroy(self) -> None: ...
    def reset_hba(self) -> None: ...
    def add_hba_entry(
        self,
        *,
        type: str = ...,
        database: str,
        user: str,
        address: Optional[Any] = ...,
        auth_method: str,
        auth_options: Optional[Any] = ...,
    ) -> Any: ...
