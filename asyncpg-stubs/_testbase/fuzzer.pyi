import socket
from asyncio import AbstractEventLoop, Event, Future, Task
from threading import Thread
from typing import Any

from asyncpg import cluster as cluster

class StopServer(Exception): ...

class TCPFuzzingProxy:
    listening_addr: str
    listening_port: int | None
    backend_host: str
    backend_port: int
    settings: dict[str, Any]
    loop: AbstractEventLoop | None
    connectivity: Event | None
    connectivity_loss: Event | None
    stop_event: Event | None
    connections: dict[Connection, Task[Any]]
    sock: socket.socket | None
    listen_task: Future[Any] | None
    def __init__(
        self,
        *,
        listening_addr: str = ...,
        listening_port: int | None = ...,
        backend_host: str,
        backend_port: int,
        settings: dict[str, Any] | None = ...,
    ) -> None: ...
    thread: Thread | None
    def start(self) -> None: ...
    def stop(self) -> None: ...
    async def listen(self) -> None: ...
    def trigger_connectivity_loss(self) -> None: ...
    def restore_connectivity(self) -> None: ...
    def reset(self) -> None: ...
    def close_all_connections(self) -> None: ...

class Connection:
    client_sock: socket.socket
    backend_sock: socket.socket
    proxy: TCPFuzzingProxy
    loop: AbstractEventLoop
    connectivity: Event
    connectivity_loss: Event
    proxy_to_backend_task: Future[Any] | None
    proxy_from_backend_task: Future[Any] | None
    is_closed: bool
    def __init__(
        self,
        client_sock: socket.socket,
        backend_sock: socket.socket,
        proxy: TCPFuzzingProxy,
    ) -> None: ...
    def close(self) -> None: ...
    async def handle(self) -> None: ...
    async def proxy_to_backend(self) -> None: ...
    async def proxy_from_backend(self) -> None: ...
