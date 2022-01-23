#!/usr/bin/bash

PWD=$(pwd)

cd "${PWD}"

source "$( poetry env list --full-path | grep internet-speedtest-pi | cut -d' ' -f1 )/bin/activate"

poetry run python run_speedtest.py

