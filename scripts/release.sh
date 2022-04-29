#!/bin/bash

set -e
shopt -s extglob

RELEASE_VERSION="${1}"; shift
DRY_RUN_FLAG="${1}"; shift

DRY_RUN=0

if [[ " ${DRY_RUN_FLAG} " == " --dry-run " ]]; then
    DRY_RUN=1
fi

function execute() {
    local dry_run="${DRY_RUN}"

    if [[ " ${1} " == " -f " ]]; then
        shift
        dry_run=0
    fi

    echo "> $@"
    if [ $dry_run -eq 0 ]; then
        "$@";
    fi
    return $?
}

function set_version() {
    local VERSION="${1}"; shift

    execute -f poetry version "${VERSION}"
}

function commit_version() {
    local MESSAGE="${1}"; shift

    execute git add --update pyproject.toml
    execute git commit -m "${MESSAGE}"
}

set_version "${RELEASE_VERSION}"

NEW_VERSION="$(poetry version -s)"

commit_version "Release ${NEW_VERSION}"
execute git tag "v${NEW_VERSION}"

set_version "pre${RELEASE_VERSION}"
commit_version "Post release version bump"

if [ $DRY_RUN -eq 1 ]; then
    git restore pyproject.toml
fi

execute git push
execute git push --tags
