from typing import Any, Dict, NamedTuple

PGPASSFILE: str

class _ConnectionParameters(NamedTuple):
    user: str
    password: str
    database: str
    ssl: bool
    ssl_is_advisory: bool
    connect_timeout: float
    server_settings: Dict[str, Any]

class _ClientConfiguration(NamedTuple):
    command_timeout: float
    statement_cache_size: int
    max_cached_statement_lifetime: float
    max_cacheable_statement_size: int
