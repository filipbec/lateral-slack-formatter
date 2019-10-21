#!/usr/bin/env bash

set -o errexit # exit script if a command fails
set -o nounset # exit if script tries to use undeclared variablesvi

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
