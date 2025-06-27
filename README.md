# asyncpg-stubs

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://github.com/bryanforbes/asyncpg-stubs/blob/master/LICENSE)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Checked with pyright](https://img.shields.io/badge/pyright-checked-informational.svg)](https://github.com/microsoft/pyright/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

This package contains type stubs to provide more precise static types and type inference for [asyncpg](https://github.com/MagicStack/asyncpg).

## Installation

```shell
pip install asyncpg-stubs
```

## Development

Make sure you have [poetry](https://python-poetry.org/) installed.

```shell
poetry install
poetry run pre-commit install --hook-type pre-commit
```

## Version numbering scheme

The **major** and **minor** version numbers of `asyncpg-stubs` will match the **major**
and **minor** version numbers of the `asyncpg` release the stubs represent. For
instance, if you are using `asyncpg` version `0.25.0`, you would use `asyncpg-stubs`
version `0.25.X` where `X` is the latest **patch** version of the stubs. Using semver
dependencty specifications, `asyncpg-stubs` version `~0.25` is designed to work with
`asyncpg` version `~0.25`.

In addition, `asyncpg-stubs` will indicate which versions of the runtime library are compatible through its dependency information (as suggested in PEP-561).
