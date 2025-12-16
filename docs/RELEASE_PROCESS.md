# Release Process

This document explains the three-stage automated release workflow for asyncpg-stubs.

## Overview

The release process separates concerns into distinct stages:

1. **Stage 1: Release PR Creation** — Automated detection of changes, version bump, and PR creation
2. **Stage 2: Tagging & Post-Release Version Bump** — Tag creation and automatic version bump for next development cycle
3. **Stage 3: Build & Publish** — Package building, GitHub release creation, and PyPI publication

This three-stage approach provides clear review gates and allows flexibility in release timing. Stages 1 and 2 run in the same workflow (`release-pr.yml`) but handle different version states.

## Architecture

### Version Scheme

asyncpg-stubs follows semantic versioning that tracks asyncpg's major and minor versions:

- **Major.minor**: Follows asyncpg's major.minor version (e.g., stubs 0.31.x for asyncpg 0.31.x)
- **Patch**: Incremented for stubs-specific fixes and features
- **Dev suffix**: `.dev0` appended during development (e.g., `0.31.2.dev0`)

### Python Version

The GitHub Actions workflows require Python 3.14. This ensures reproducible builds and consistency across all workflow runs.

### Branch Strategy

**Production**:
- **master**: Main development branch
- **release**: PR branch where release commits are created (automatically managed by script)
- **Tags**: Production version tags matching pattern `v[0-9]+.*` (e.g., `v0.31.2`) trigger publication workflow

**Testing**:
- **test/master**: Test branch for release testing (bypasses some safety checks)
- **test/release**: Test PR branch (automatically managed)
- **Tags**: Test version tags matching pattern `test-v[0-9]+.*` (e.g., `test-v0.31.2`) allow testing publishing workflow without PyPI publication

### Git Cliff Integration

The project uses [git-cliff](https://github.com/orhun/git-cliff) for automated changelog generation.

**Commit filtering** (via `cliff.toml`):
- **Included**: `feat:`, `fix:`, `feat!:` commits → releasable
- **Included**: `chore(deps): update dependency asyncpg to ...` → releasable (version bump triggers)
- **Excluded**: `chore(dev):`, `chore(pr):`, `chore(pull):`, `chore(deps):` (non-asyncpg), `docs:`, `style:`, `test:`, `ci:`, `release:` commits

## Stage 1: Release PR Creation

**Triggers**:
- Push to `master` (normal mode)
- Push to `test/master` (test mode)
- Manual `workflow_dispatch` with optional `test_mode` input

**Script**: `mise run release-pr` (defined in `mise-tasks/release-pr`)

**Workflow**: `.github/workflows/release-pr.yml`

**Test Mode**: Automatically enabled when pushing to `test/master` or via `workflow_dispatch` with `test_mode=true`. In test mode:
- Uses `test/master` as base branch and `test/release` as PR branch
- Creates `test-v` prefixed tags instead of `v` prefixed
- Labels PRs with `[TEST MODE]` prefix in title
- Still runs release logic but prevents accidental publishing

### Flow

1. **Extract Current Version** from `pyproject.toml`
   - Example: `0.31.2.dev0`

2. **Check for Dev Suffix**
   - If version lacks `.dev0`: Skip to Stage 2 (tagging)
   - If version has `.dev0`: Continue with PR creation

3. **Check for Releasable Commits**
   - Run: `git cliff --unreleased --strip all`
   - If output is empty or only has header: Exit silently (no release needed)
   - If output has content: Continue to version bump

4. **Determine Version Bump**
   - If changelog contains `chore(deps): update dependency asyncpg to >=X.Y,<...>`:
     - Parse new asyncpg major.minor
     - Set stubs version to `<X.Y>.0` (e.g., `0.32.0`)
   - Otherwise (feat/fix commits):
     - Bump patch only (e.g., `0.31.2` → `0.31.3`)

5. **Update Files**
   - Update `pyproject.toml` with new version
   - Update `CHANGELOG.md` using `git cliff --prepend`

6. **Create/Update Release PR**
    - Create or reset to `release` branch (or `test/release` in test mode)
    - Commit changes
    - Force-push to branch
    - Create or update PR targeting `master` (or `test/master` in test mode)
    - Title: `chore(release): X.Y.Z` (or `[TEST MODE] chore(release): X.Y.Z` in test mode)
    - Body: changelog entries from git-cliff
    - Add `release` label to PR

### Developer Action

Review the release PR:
- Verify version bump is correct (check asyncpg version if applicable)
- Review changelog entries for accuracy
- Merge PR to `master`

## Stage 2: Tagging & Post-Release Version Bump

**Triggers**: Push to `master` from Stage 1 PR merge (merge of release PR bumps version, triggering Stage 2)

**Script**: `mise run release-pr` (same `release-pr.yml` workflow detects release version and creates tags)

**Workflow**: `.github/workflows/release-pr.yml`

**Important**: Stage 2 creates tags but does NOT build or publish. Publishing happens in Stage 3, automatically triggered when the tag is pushed to origin.

### Flow

1. **Extract Current Version** from `pyproject.toml`
   - Example: `0.31.3` (no `.dev0` suffix)

2. **Check for Dev Suffix**
   - If version has `.dev0`: Return to Stage 1
   - If version lacks `.dev0`: Continue with tagging

3. **Check if Already Tagged**
   - Look for git tag `v<VERSION>`
   - If tag exists: Exit (version already handled)
   - If tag missing: Continue

4. **Create and Push Tag**
   - Create annotated tag: `v<VERSION>`
   - Push tags to origin (automatically triggers `release.yml`)

5. **Post-Release Version Bump**
   - Calculate next patch version: increment patch, append `.dev0`
   - Example: `0.31.3` → `0.31.4.dev0`
   - Update `pyproject.toml`
   - Commit: `chore(release): post-release version bump`
   - Push commit to `master`

### Result

- Git tag is pushed to origin
- Tag push triggers `.github/workflows/release.yml`
- Development continues with next `.dev0` version
- Ready for Stage 3 (publishing)

## Stage 3: Build & Publish

**Triggers**:
- Push of production version tag matching pattern `v[0-9]+.*` from Stage 2
- Push of test version tag matching pattern `test-v[0-9]+.*` from Stage 2
- Manual `workflow_dispatch` with version (without leading `v`) and optional test_mode input

**Script**: `mise run release --tag-name=<tag>` (defined in `mise-tasks/release`)

**Workflow**: `.github/workflows/release.yml`

**Test Mode**: Automatically enabled when tag starts with `test-v` or via `workflow_dispatch` with `test_mode=true`. In test mode:
- Skips PyPI publishing
- Marks GitHub release title as `[TEST MODE] <tag>`
- Prepends warning to release notes indicating it was not published

### Flow

1. **Install Dependencies**
    - Run `poetry install -v --only main --no-interaction` to prepare the environment for building
    - This step is required before building the package

2. **Build Package**
    - Run `poetry build -vvv` to create wheel and sdist artifacts in `dist/` directory
    - Verbose output helps diagnose build issues

3. **Publish to PyPI** (skipped in test mode)
    - Run `poetry publish -n` to publish wheel and sdist
    - Version is now available via `pip install asyncpg-stubs`
    - Requires `POETRY_PYPI_TOKEN_PYPI` environment variable (GitHub secret)

4. **Generate Release Notes**
    - Run `git cliff --latest --strip header` to extract changelog entries for this release
    - Release notes are written to temporary file (`/tmp/release-notes.md`)

5. **Create GitHub Release**
    - Run `gh release create` with tag name, title, notes file, and artifacts
    - Attach built artifacts from `dist/*` to the release
    - Release title is tag name, or `[TEST MODE] <tag>` in test mode
    - In test mode: prepend warning message to release notes indicating it was not published to PyPI

### Result

**Production**:
- Package is published to PyPI
- GitHub release is created
- Release cycle is complete
- Next development cycle begins with `.dev0` version

**Test Mode**:
- GitHub release is created (marked `[TEST MODE]`)
- Package is NOT published to PyPI
- Release notes include warning about test status
- Useful for validating entire release workflow before real publication

## Complete Example

### Scenario: Feature Addition

```
Day 1: Developer commits
- Commit: "feat: add stubs for new asyncpg method"
- Push to master

Stage 1 Triggered (release-pr.yml):
- Detects releasable commit (feat)
- Version: 0.31.2.dev0
- Bump patch: 0.31.2.dev0 → 0.31.2
- Create release PR with title "chore(release): 0.31.2"
- PR body: changelog entries from git-cliff

Day 2: Review & Merge
- Developer reviews PR
- Merges PR to master
- Merge commit pushed

Stage 2 Triggered (release-pr.yml):
- Detects release version (0.31.2, no .dev0)
- Creates tag v0.31.2
- Pushes tag to origin (triggers release.yml)
- Bumps version: 0.31.2 → 0.31.3.dev0
- Commits and pushes post-release bump

Stage 3 Triggered (release.yml):
- Triggered by v0.31.2 tag push
- Builds wheel and sdist
- Creates GitHub release
- Publishes to PyPI
- asyncpg-stubs 0.31.2 now available via pip

Development Continues:
- master now has 0.31.3.dev0
- Ready for next changes
```

### Scenario: asyncpg Version Update

```
Scenario: asyncpg upgrades from 0.31.x to 0.32.x

Day 1: Renovate Update
- Renovate creates PR with commit:
  "chore(deps): update dependency asyncpg to >=0.32,<0.33"
- Developer reviews and merges Renovate PR

Stage 1 Triggered (release-pr.yml):
- Detects releasable commit (asyncpg version change)
- Parses new version: 0.32 from constraint >=0.32,<0.33
- Detects asyncpg major/minor changed
- Version: 0.31.5.dev0
- Bump version: 0.31.5.dev0 → 0.32.0 (reset patch to 0)
- Create release PR with title "chore(release): 0.32.0"

Day 2: Review & Merge
- Developer merges release PR

Stage 2 & 3:
- Tag v0.32.0 created and pushed
- release.yml builds and publishes
- asyncpg-stubs 0.32.0 published (now compatible with asyncpg 0.32.x)
```

### Scenario: No Releasable Changes

```
Scenario: Only dependency lock file updates

Developer commits:
- Commit: "chore(dev): update poetry.lock"
- Push to master

Stage 1 Triggered (release-pr.yml):
- Detects dev suffix in version (0.31.2.dev0)
- Runs git-cliff to find releasable commits
- git-cliff output: empty (only lock file, not in releasable commits)
- Exits silently
- No PR created
- Development continues unchanged
```

## Testing and Debugging

### Dry-Run Mode

Both release scripts support `--dry-run` for testing without making changes:

```bash
mise run release-pr --dry-run
mise run release --dry-run --tag-name=v0.31.3
```

**Default behavior**:
- **Manual calls** (`mise run`): Dry-run mode is enabled by default (`--dry-run`)
- **GitHub Actions workflows**: Dry-run is enabled by default **except** in test mode
  - `release-pr.yml`: Runs with dry-run ENABLED in normal/production mode, disabled in test mode
  - `release.yml`: Runs with dry-run ENABLED in normal/production mode, disabled in test mode
- Override with `--no-dry-run` flag to actually execute commands

In dry-run mode:
- Extracts and logs version information
- Checks for releasable commits
- Simulates version bump logic
- Echoes commands prefixed with `[DRY RUN]` instead of executing them
- Makes NO changes to files or git history

Useful for:
- Verifying version bump logic locally
- Testing changelog detection
- Understanding what would happen on next push
- Debugging release workflows without making actual changes

### Test Mode

Use test mode to validate the complete release workflow without publishing to PyPI:

**Via Git branches**:
```bash
git checkout -b test/master
git push origin test/master
# release-pr.yml automatically runs in test mode
# Creates test/release branch and test-v* tags
```

**Via workflow dispatch**:
```bash
gh workflow run release-pr.yml -f test_mode=true
# For release.yml, provide version without leading 'v'
gh workflow run release.yml -f version=0.31.3 -f test_mode=true
```

Test mode allows:
- Creating release PRs with `[TEST MODE]` prefix
- Testing tag creation without triggering real publishing
- Creating GitHub releases without PyPI publication
- Validating the complete workflow before production release

After testing, clean up test artifacts:
```bash
git push origin --delete test/master test/release
git push origin --delete-refs refs/tags/test-v*
```

## Automation with Git Workflow

### Environment Variable Overrides

GitHub Actions workflows set environment variables that override script defaults:
- `MISE_ENV=ci` — Sets mise to CI mode
- `DRY_RUN` — Set by workflow; overrides script default
- `TEST_MODE` — Set by workflow; overrides script default

The workflow-set values take precedence over script flag defaults.

### Concurrency Control

The `release-pr.yml` workflow uses concurrency control (`group: release-pr`) to ensure only one release PR creation process runs at a time. If a new push to `master` occurs before the previous workflow completes, the new run queues and waits for the in-progress run to finish. This prevents multiple simultaneous release operations from conflicting.

### On Push to master

1. `release-pr.yml` workflow triggers (with `DRY_RUN=true` in production mode, `DRY_RUN=false` in test mode)
2. Runs `mise run release-pr`
3. Script checks current version:
   - If `.dev0` suffix: Attempt Stage 1 (create PR)
   - If no `.dev0`: Attempt Stage 2 (create tag)

### On PR Merge to master

1. Merge commit is pushed (pyproject.toml now has version without `.dev0`)
2. `release-pr.yml` triggers again
3. Script detects release version (no `.dev0`)
4. Stage 2 runs: Creates tag, bumps to next `.dev0`, pushes tag and commit

### On Tag Push

1. `release.yml` workflow triggers on tags matching `v[0-9]+.*` or `test-v[0-9]+.*`
2. Extracts tag name and determines test mode (if tag starts with `test-v`)
3. Stage 3 runs:
    - Installs dependencies with Poetry
    - Builds package (wheel and sdist)
    - Publishes to PyPI via `poetry publish` (skipped if test mode)
    - Generates release notes using `git cliff --latest --strip header`
    - Creates GitHub release with `gh release create` (includes title, notes, and artifacts)
    - Prepends test mode warning to notes if applicable

## Manual Release (If Needed)

### Manually Trigger Release PR Workflow

```bash
gh workflow run release-pr.yml
```

Or via GitHub Actions UI:
1. Go to Actions → "Create Release PR"
2. Click "Run workflow"
3. Optionally set `test_mode=true` for test mode
4. Workflow will immediately run on current master

### Manually Trigger Release Workflow (Stage 3)

```bash
# For production release with version 0.31.3
gh workflow run release.yml -f version=0.31.3

# For test mode
gh workflow run release.yml -f version=0.31.3 -f test_mode=true
```

**Note**: The `version` parameter should be provided without the leading `v`. The workflow will automatically prepend `v` to create the tag name.

## Environment Requirements

The automated workflows require:

- **gh CLI**: GitHub's command-line tool (for PR operations)
- **git-cliff**: Changelog generation (already in mise.toml)
- **Poetry**: Python package management (already in mise.toml)
- **GITHUB_TOKEN**: GitHub API authentication (provided by GitHub Actions)

## Permissions

The release workflows require these GitHub permissions:

- `contents: write` — Push commits and tags
- `pull-requests: write` — Create and update PRs

## Related Files

- **mise-tasks/release-pr** — Release automation script
- **.github/workflows/release-pr.yml** — PR creation and tagging workflow
- **.github/workflows/release.yml** — Building and publishing workflow
- **cliff.toml** — git-cliff configuration for changelog filtering
- **pyproject.toml** — Package version and metadata
- **CHANGELOG.md** — Auto-generated changelog

## Troubleshooting

### No PR created on push to master

Check if there are releasable commits:
```bash
git cliff --unreleased --strip all
```

If output is empty, no commits match the releasable filter. See git Cliff Integration section.

### Script errors in GitHub Actions

Enable debug logging:
1. Set secret `ACTIONS_STEP_DEBUG` to `true` in repository settings
2. Re-run the workflow
3. View detailed logs in workflow run

### Tag already exists but release.yml didn't run

The tag exists but the version was never published. Manually trigger release.yml:
```bash
gh workflow run release.yml
```

Or check the tag was pushed correctly:
```bash
git tag -l | grep v0.31.3
```
