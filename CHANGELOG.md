# Changelog

## [0.31.2](https://github.com/bryanforbes/asyncpg-stubs/compare/v0.31.1..v0.31.2) - 2025-12-17

### Bug Fixes

- **prepared_stmt** test commit ([97023e8](https://github.com/bryanforbes/asyncpg-stubs/commit/97023e84b6b5cb20e4b4de6bb00a0d6cffc5a4c2))
- **prepared_stmt** revert test commit ([a20aabd](https://github.com/bryanforbes/asyncpg-stubs/commit/a20aabde67c674b6be4b931cef66b7fea60b765f))

## [0.31.1](https://github.com/bryanforbes/asyncpg-stubs/compare/v0.31.0..v0.31.1) - 2025-12-10

### Bug Fixes

- **prepared_stmt** `fetchmany()` and `execute()` signatures ([#405](https://github.com/bryanforbes/asyncpg-stubs/pull/405))

## [0.31.0](https://github.com/bryanforbes/asyncpg-stubs/compare/v0.30.2..v0.31.0) - 2025-12-01

### Features

- updates for v0.31.0 ([8a188d1](https://github.com/bryanforbes/asyncpg-stubs/commit/8a188d147e75e80641c304f559b5f79781aa6aa6))

### Dependency Updates

- update dependency typing-extensions to v4.15.0 ([#392](https://github.com/bryanforbes/asyncpg-stubs/pull/392))
- update dependency asyncpg to >=0.31,<0.32 ([#396](https://github.com/bryanforbes/asyncpg-stubs/pull/396))
- update dependency typing-extensions to v4.15.0 ([#398](https://github.com/bryanforbes/asyncpg-stubs/pull/398))

## [0.30.2](https://github.com/bryanforbes/asyncpg-stubs/compare/v0.30.1..v0.30.2) - 2025-06-27

### Features

- add `TypeVar` defaults ([#377](https://github.com/bryanforbes/asyncpg-stubs/pull/377))

### Dependency Updates

- update dependency typing-extensions to v4.13.2 ([#366](https://github.com/bryanforbes/asyncpg-stubs/pull/366))

### Miscellaneous

- switch to `ruff format` from `black` ([d8ca48f](https://github.com/bryanforbes/asyncpg-stubs/commit/d8ca48fa0430d0661c99c5d8928f343ec97817a1))

## [0.30.1](https://github.com/bryanforbes/asyncpg-stubs/compare/v0.30.0..v0.30.1) - 2025-03-14

### Bug Fixes

- update return value of `Pool.__await__()` ([355b86e](https://github.com/bryanforbes/asyncpg-stubs/commit/355b86e53899b1be208b967686d664c6843d78d2))
- update tests for `Pool` ([05d26e2](https://github.com/bryanforbes/asyncpg-stubs/commit/05d26e222e89c6e2ec990e478cdf6b72f5229fad))

## [0.30.0](https://github.com/bryanforbes/asyncpg-stubs/compare/v0.29.0..v0.30.0) - 2024-11-04

### Features

- Begin work for 0.30 ([5931025](https://github.com/bryanforbes/asyncpg-stubs/commit/5931025914e731503cfd79f587d7f9389c49ffce))
- Update API for GSSAPI authentication ([ffd43bb](https://github.com/bryanforbes/asyncpg-stubs/commit/ffd43bb1852e0f4a8d13eee460836a70c7b0f514))
- Update API for SSPI authentication ([700e319](https://github.com/bryanforbes/asyncpg-stubs/commit/700e31926f33e0317d0bf0a9c633499595e9fb66))
- support asyncpg v0.30.0 ([b662a36](https://github.com/bryanforbes/asyncpg-stubs/commit/b662a360348c5b724fe18563f06659e6cf1945b1))

### Bug Fixes

- problems found with stubtest ([994d5f0](https://github.com/bryanforbes/asyncpg-stubs/commit/994d5f02dc2ae6b378867a072b336f53b48c239f))

### Dependency Updates

- Update dependency typing-extensions to v4.9.0 ([#260](https://github.com/bryanforbes/asyncpg-stubs/pull/260))
- Update dependency typing-extensions to v4.10.0 ([#282](https://github.com/bryanforbes/asyncpg-stubs/pull/282))
- Update dependency typing-extensions to v4.11.0 ([#296](https://github.com/bryanforbes/asyncpg-stubs/pull/296))
- Update dependency typing-extensions to v4.12.0 ([#313](https://github.com/bryanforbes/asyncpg-stubs/pull/313))
- Update dependency typing-extensions to v4.12.1 ([#320](https://github.com/bryanforbes/asyncpg-stubs/pull/320))
- Update dependency typing-extensions to v4.12.2 ([#324](https://github.com/bryanforbes/asyncpg-stubs/pull/324))
- update dependency asyncpg to >=0.30,<0.31 ([#350](https://github.com/bryanforbes/asyncpg-stubs/pull/350))

### Miscellaneous

- Move async-timeout to dev dependency ([ad84097](https://github.com/bryanforbes/asyncpg-stubs/commit/ad8409700a86cecdc987b506d432e755aeb4449e))

## [0.29.0](https://github.com/bryanforbes/asyncpg-stubs/compare/v0.28.0..v0.29.0) - 2023-11-05

### Features

- Begin work for 0.29 ([ceaebdd](https://github.com/bryanforbes/asyncpg-stubs/commit/ceaebddb58255a8acae9a12e8b55be4ebe6f4ab7))
- Bring up to date with asyncpg master ([6cfdc29](https://github.com/bryanforbes/asyncpg-stubs/commit/6cfdc2941ffafefb217e53ebc1696671fa61f005))
- Update types for 3.8 and fix problems found with `stubtest` ([6c245af](https://github.com/bryanforbes/asyncpg-stubs/commit/6c245af3fe2c31af8bea1f307b2dadc84432b28d))
- Bump minimum `typing_extensions` version for Python 3.12 support ([63e7340](https://github.com/bryanforbes/asyncpg-stubs/commit/63e7340bb5f1c8672081edc601425a977be490b7))

### Dependency Updates

- Update dependency typing-extensions to v4.8.0 ([#221](https://github.com/bryanforbes/asyncpg-stubs/pull/221))
- Update dependency asyncpg to >=0.29,<0.30 ([#243](https://github.com/bryanforbes/asyncpg-stubs/pull/243))

## [0.28.0](https://github.com/bryanforbes/asyncpg-stubs/compare/v0.27.1..v0.28.0) - 2023-07-09

### Features

- Update stubs for 0.28.0 ([782ed09](https://github.com/bryanforbes/asyncpg-stubs/commit/782ed09137f424b70d5886700fdeacf6c3021743))

### Dependency Updates

- Update dependency asyncpg to >=0.28,<0.29 ([#178](https://github.com/bryanforbes/asyncpg-stubs/pull/178))

## [0.27.1](https://github.com/bryanforbes/asyncpg-stubs/compare/v0.27.0..v0.27.1) - 2023-07-09

### Features

- Update typings and add more tests ([209e09a](https://github.com/bryanforbes/asyncpg-stubs/commit/209e09a88eb7cd6455776a9bce794772773446df))

### Dependency Updates

- Bump typing-extensions from 4.4.0 to 4.5.0 ([#134](https://github.com/bryanforbes/asyncpg-stubs/pull/134))
- Update dependency typing-extensions to v4.6.2 ([#168](https://github.com/bryanforbes/asyncpg-stubs/pull/168))
- Update dependency typing-extensions to v4.6.3 ([#172](https://github.com/bryanforbes/asyncpg-stubs/pull/172))

### Miscellaneous

- Switch to using ruff ([#154](https://github.com/bryanforbes/asyncpg-stubs/pull/154))

## [0.27.0](https://github.com/bryanforbes/asyncpg-stubs/compare/v0.26.6..v0.27.0) - 2022-10-26

### Features

- Changes for asyncpg 0.27.0 ([7dd93e3](https://github.com/bryanforbes/asyncpg-stubs/commit/7dd93e3f68b8dc698543e75a2e935b8e8fb3ad36))

## [0.26.6](https://github.com/bryanforbes/asyncpg-stubs/compare/v0.26.5..v0.26.6) - 2022-10-25

### Revert

- Revert typing of `asyncpg.create_pool()` and add test ([94eaa96](https://github.com/bryanforbes/asyncpg-stubs/commit/94eaa963efc612018e8e89f08a7366d8e950d9f4))

## [0.26.5](https://github.com/bryanforbes/asyncpg-stubs/compare/v0.26.4..v0.26.5) - 2022-10-24

### Bug Fixes

- Fix typing for `asyncpg.create_pool()` ([e387d77](https://github.com/bryanforbes/asyncpg-stubs/commit/e387d77f6af463e8cebe3e4601ed44adfb9cc6d0))

## [0.26.4](https://github.com/bryanforbes/asyncpg-stubs/compare/v0.26.3..v0.26.4) - 2022-10-07

### Bug Fixes

- Remove positional-only notation for mypy 0.980+ ([27608fe](https://github.com/bryanforbes/asyncpg-stubs/commit/27608feb4ca4243e4c83ce505587bcc2a6ca6b2a))
- Fix `_RangeValue` protocol ([8e99563](https://github.com/bryanforbes/asyncpg-stubs/commit/8e995635162f646a0500d267c4107cc30ba81eaa))

## [0.26.3](https://github.com/bryanforbes/asyncpg-stubs/compare/v0.26.2..v0.26.3) - 2022-09-22

### Features

- Improve typing ([4576760](https://github.com/bryanforbes/asyncpg-stubs/commit/45767605183bc05892b65f47f7bfa0f39f1afe89))

## [0.26.2](https://github.com/bryanforbes/asyncpg-stubs/compare/v0.26.1..v0.26.2) - 2022-07-29

### Features

- Improve `connect(port=)` typing ([5ea9a49](https://github.com/bryanforbes/asyncpg-stubs/commit/5ea9a49056b1142def36ac274cc14f709a35352c))

## [0.26.1](https://github.com/bryanforbes/asyncpg-stubs/compare/v0.26.0..v0.26.1) - 2022-07-26

### Features

- Tweaks based on work for asyncpg typings ([d0cbeb2](https://github.com/bryanforbes/asyncpg-stubs/commit/d0cbeb2af369050ddeedc2c2509b40cf3d1affa0))

## [0.26.0](https://github.com/bryanforbes/asyncpg-stubs/compare/v0.25.4..v0.26.0) - 2022-07-25

### Features

- Updates for 0.26.0 ([ea06672](https://github.com/bryanforbes/asyncpg-stubs/commit/ea066725ebfc62e9dd1983a3716f43d0c1145b92))

### Dependency Updates

- Bump asyncpg from 0.25.0 to 0.26.0 ([#106](https://github.com/bryanforbes/asyncpg-stubs/pull/106))
- Bump typing-extensions from 4.2.0 to 4.3.0 ([#105](https://github.com/bryanforbes/asyncpg-stubs/pull/105))

## [0.25.4](https://github.com/bryanforbes/asyncpg-stubs/compare/v0.25.3..v0.25.4) - 2022-05-31

### Bug Fixes

- Remove `Self` from import ([6612014](https://github.com/bryanforbes/asyncpg-stubs/commit/66120143b0a54a6eda04b962a13653e80cd5ebd2))
- Fix typing for APIs that use `tempfile.mkdtemp()` ([81dbb53](https://github.com/bryanforbes/asyncpg-stubs/commit/81dbb53a9a1d46e79fb9f909a62255d7503c46ce))

## [0.25.3](https://github.com/bryanforbes/asyncpg-stubs/compare/v0.25.2..v0.25.3) - 2022-05-25

### Features

- Improve types for `Range` ([e0b393d](https://github.com/bryanforbes/asyncpg-stubs/commit/e0b393d5fe2b0ae411554d7ab145b11595fd5ba7))

## [0.25.2](https://github.com/bryanforbes/asyncpg-stubs/compare/v0.25.1..v0.25.2) - 2022-05-10

### Miscellaneous

- Fix flake8-pyi errors ([6313b4b](https://github.com/bryanforbes/asyncpg-stubs/commit/6313b4bd5520d2b633fe2487436516ebf34a2822))

## [0.25.1](https://github.com/bryanforbes/asyncpg-stubs/tree/v0.25.1) - 2022-04-29

### Features

- Initial release
