#!/bin/sh

set -e

# activate virtual env
. /opt/pysetup/.venv/bin/activate

# Additional setup logic goes here



# Evaluating a passed command:
exec "$@"
