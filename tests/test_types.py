from datetime import datetime
from typing_extensions import assert_type

from asyncpg.types import Range

r1 = Range(0, 20)
assert_type(r1, 'Range[int]')

r2 = Range(datetime(1982, 6, 26), datetime(2024, 6, 26))
assert_type(r2, 'Range[datetime]')
