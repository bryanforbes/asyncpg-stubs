# asyncpg-stubs Agent Guidelines

## Build, Test & Lint

- **Setup**: `poetry install --all-extras && poetry run pre-commit install --hook-type pre-commit`
- **Lint**: `poetry run ruff check .` (also check format: `poetry run ruff format --check .`)
- **Format**: `poetry run ruff format .`
- **Type Check**: `poetry run mypy` and `poetry run pyright`
- **All pre-commit checks**: `poetry run pre-commit run --all-files`

## Architecture

This is a **type stubs** package (`.pyi` files) for the asyncpg PostgreSQL async driver. Core modules:
- **asyncpg-stubs/**: Type definition files for asyncpg APIs (connection, pool, cursors, transactions, exceptions, etc.)
- **tests/**: Test suite validating stub correctness (type checking tests)
- Version scheme: semver matches asyncpg versions (e.g., stubs 0.30.x for asyncpg 0.30.x)

## Code Style

- **Python version**: 3.9+
- **Line length**: 88 chars
- **Quotes**: Single quotes
- **Imports**: Use `isort` config (`typing_extensions`, `_types`, `_typeshed` as stdlib)
- **Type checking**: Strict mode (mypy `strict=true`, pyright `strict` mode)
- **Formatting**: Ruff handles all formatting/linting
- **.pyi files**: Exempt from some rules (E501, E741, F401-F405, F811)
- **Tests**: Allow assertions (S101), relax some style rules

## Git Conventions

- **Commit messages**: Use [conventional commits](https://www.conventionalcommits.org/) with 50/72 rule
  - Format: `<type>(<scope>): <description>`
  - Types:
    - `chore`: changes to build process, auxiliary tools/libraries, or releases
    - `ci`: changes to CI configuration/scripts
    - `docs`: documentation only changes
    - `feat`: a new feature
    - `fix`: a bug fix
    - `perf`: a code change that improves performance (probably not relevant for this project)
    - `refactor`: a code change that neither fixes a bug nor adds a feature
    - `style`: changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
    - `test`: adding missing tests or correcting existing tests
  - Scope: Optional, e.g., `(prepared_stmt)`, `(github)`, `(ruff)`, `(release)`
  - **Subject line**: Max 50 characters, lowercase, no period, imperative mood
  - **Body**: Wrap at 72 characters, add after blank line if explanation needed
  - **Amp analysis commits**: Include thread reference and co-author at end of message:
    - `Amp-Thread-ID: https://ampcode.com/threads/T-<uuid>`
    - `Co-authored-by: Amp <amp@ampcode.com>`
    - If there are multiple amp threads, they should all be ordered by ascending date, one line each, before the
      co-author line
  - Example:
    ```text
    ci(mise): implement steps 1-2 of release process

    - refine cliff.toml to skip CI-related commits and filter deps properly
    - create mise-tasks/start-release script with full release workflow
    - add --dry-run flag for local testing
    - fix changelog detection to only trigger on actual commits
    - fix version comparison logic to check commits first
    - update RELEASE_PLAN.md and RELEASE_TODO.md with testing info and
      refinements

    Amp-Thread-ID: https://ampcode.com/threads/T-019b1fbc-c5a3-7400-bfdf-71702b66bbb9
    Co-authored-by: Amp <amp@ampcode.com>
    ```
