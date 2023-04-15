#!/usr/bin/env bash

# Usage:
# From project root, ./env_aware_make_everything.sh

direnv allow .
eval "$(direnv export bash)"
make everything
