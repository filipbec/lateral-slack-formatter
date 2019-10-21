#!/usr/bin/env bash

set -o errexit # exit script if a command fails
set -o nounset # exit if script tries to use undeclared variables

source venv/bin/activate
python lateral.py
