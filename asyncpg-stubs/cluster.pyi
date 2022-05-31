from _typeshed import BytesPath, StrPath
from asyncio import AbstractEventLoop
from typing import Any, overload
from typing_extensions import TypedDict

from . import connection, types

class _ConnectionSpec(TypedDict):
    host: str
    port: str

def platform_exe(name: str) -> str: ...
def find_available_port() -> int | None: ...

class ClusterError(Exception): ...

class Cluster:
    def __init__(self, data_dir: str, *, pg_config_path: str | None = ...) -> None: ...
    def get_pg_version(self) -> types.ServerVersion: ...
    def is_managed(self) -> bool: ...
    def get_data_dir(self) -> str: ...
    def get_status(self) -> str: ...
    async def connect(
        self,
        loop: AbstractEventLoop | None = ...,
        **kwargs: Any,
    ) -> connection.Connection[Any]: ...
    def init(self, **settings: str) -> str: ...
    def start(
        self,
        wait: int = ...,
        *,
        server_settings: dict[str, str] = ...,
        **opts: Any,
    ) -> None: ...
    def reload(self) -> None: ...
    def stop(self, wait: int = ...) -> None: ...
    def destroy(self) -> None: ...
    def get_connection_spec(self) -> _ConnectionSpec: ...
    def override_connection_spec(self, **kwargs: str) -> None: ...
    def reset_wal(self, *, oid: int | None = ..., xid: int | None = ...) -> None: ...
    def reset_hba(self) -> None: ...
    def add_hba_entry(
        self,
        *,
        type: str = ...,
        database: str,
        user: str,
        address: str | None = ...,
        auth_method: str,
        auth_options: dict[str, str] | None = ...,
    ) -> None: ...
    def trust_local_connections(self) -> None: ...
    def trust_local_replication_by(self, user: str) -> None: ...

class TempCluster(Cluster):
    @overload
    def __init__(
        self,
        *,
        data_dir_suffix: str | None = ...,
        data_dir_prefix: str | None = ...,
        data_dir_parent: StrPath | None = ...,
        pg_config_path: str | None = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        data_dir_suffix: bytes | None = ...,
        data_dir_prefix: bytes | None = ...,
        data_dir_parent: BytesPath | None = ...,
        pg_config_path: str | None = ...,
    ) -> None: ...

class HotStandbyCluster(TempCluster):
    @overload
    def __init__(
        self,
        *,
        master: _ConnectionSpec,
        replication_user: str,
        data_dir_suffix: str | None = ...,
        data_dir_prefix: str | None = ...,
        data_dir_parent: StrPath | None = ...,
        pg_config_path: str | None = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        master: _ConnectionSpec,
        replication_user: str,
        data_dir_suffix: bytes | None = ...,
        data_dir_prefix: bytes | None = ...,
        data_dir_parent: BytesPath | None = ...,
        pg_config_path: str | None = ...,
    ) -> None: ...
    def init(self, **settings: str) -> str: ...
    def start(
        self,
        wait: int = ...,
        *,
        server_settings: dict[str, str] = ...,
        **opts: str,
    ) -> None: ...

class RunningCluster(Cluster):
    conn_spec: _ConnectionSpec
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
        address: str | None = ...,
        auth_method: str,
        auth_options: dict[str, str] | None = ...,
    ) -> None: ...
