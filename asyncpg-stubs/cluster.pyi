from asyncio import AbstractEventLoop
from ssl import SSLContext
from tempfile import _DirT
from typing import Any, Callable, Dict, Optional, Tuple, Type, TypeVar, Union, overload
from typing_extensions import TypedDict

from . import connect_utils
from .connection import Connection, _PasswordType
from .types import ServerVersion

class _ConnectionSpec(TypedDict):
    host: str
    port: str

def platform_exe(name: str) -> str: ...
def find_available_port(
    port_range: Tuple[int, int] = ..., max_tries: int = ...
) -> Optional[int]: ...

class ClusterError(Exception): ...

_Connection = TypeVar('_Connection', bound=Connection)

class Cluster:
    def __init__(
        self, data_dir: str, *, pg_config_path: Optional[str] = ...
    ) -> None: ...
    def get_pg_version(self) -> ServerVersion: ...
    def is_managed(self) -> bool: ...
    def get_data_dir(self) -> str: ...
    def get_status(self) -> str: ...
    @overload
    def connect(
        self,
        loop: Optional[AbstractEventLoop] = ...,
        *,
        dsn: Optional[str] = ...,
        host: Optional[connect_utils._HostType] = ...,
        port: Optional[connect_utils._PortType] = ...,
        user: Optional[str] = ...,
        password: Optional[_PasswordType] = ...,
        passfile: Optional[str] = ...,
        database: Optional[str] = ...,
        timeout: float = ...,
        statement_cache_size: int = ...,
        max_cached_statement_lifetime: int = ...,
        max_cacheable_statement_size: int = ...,
        command_timeout: Optional[float] = ...,
        ssl: Optional[connect_utils._SSLType] = ...,
        server_settings: Optional[Dict[str, str]] = ...,
    ) -> Connection: ...
    @overload
    def connect(
        self,
        loop: Optional[AbstractEventLoop] = ...,
        *,
        dsn: Optional[str] = ...,
        host: Optional[connect_utils._HostType] = ...,
        port: Optional[connect_utils._PortType] = ...,
        user: Optional[str] = ...,
        password: Optional[_PasswordType] = ...,
        passfile: Optional[str] = ...,
        database: Optional[str] = ...,
        timeout: float = ...,
        statement_cache_size: int = ...,
        max_cached_statement_lifetime: int = ...,
        max_cacheable_statement_size: int = ...,
        command_timeout: Optional[float] = ...,
        ssl: Optional[connect_utils._SSLType] = ...,
        connection_class: Type[_Connection],
        server_settings: Optional[Dict[str, str]] = ...,
    ) -> _Connection: ...
    def init(self, **settings: Any) -> str: ...
    def start(
        self, wait: int = ..., *, server_settings: Dict[str, str] = ..., **opts: Any
    ) -> None: ...
    def reload(self) -> None: ...
    def stop(self, wait: int = ...) -> None: ...
    def destroy(self) -> None: ...
    def get_connection_spec(self) -> _ConnectionSpec: ...
    def override_connection_spec(self, **kwargs: Any) -> None: ...
    def reset_wal(
        self, *, oid: Optional[int] = ..., xid: Optional[int] = ...
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
        auth_options: Optional[Dict[str, str]] = ...,
    ) -> None: ...
    def trust_local_connections(self) -> None: ...
    def trust_local_replication_by(self, user: str) -> None: ...

class TempCluster(Cluster):
    def __init__(
        self,
        *,
        data_dir_suffix: Optional[str] = ...,
        data_dir_prefix: Optional[str] = ...,
        data_dir_parent: Optional[_DirT[str]] = ...,
        pg_config_path: Optional[str] = ...,
    ) -> None: ...

class HotStandbyCluster(TempCluster):
    def __init__(
        self,
        *,
        master: _ConnectionSpec,
        replication_user: str,
        data_dir_suffix: Optional[str] = ...,
        data_dir_prefix: Optional[str] = ...,
        data_dir_parent: Optional[_DirT[str]] = ...,
        pg_config_path: Optional[str] = ...,
    ) -> None: ...
    def init(self, **settings: str) -> str: ...

class RunningCluster(Cluster):
    conn_spec: _ConnectionSpec = ...
    def __init__(self, **kwargs: str) -> None: ...
    def is_managed(self) -> bool: ...
    def get_connection_spec(self) -> _ConnectionSpec: ...
    def get_status(self) -> str: ...
    def init(self, **settings: str) -> str: ...
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
        address: Optional[str] = ...,
        auth_method: str,
        auth_options: Optional[Dict[str, str]] = ...,
    ) -> None: ...
