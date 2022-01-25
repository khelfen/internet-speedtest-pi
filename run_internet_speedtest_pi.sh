#!/usr/bin/bash

# cd into repo dir
cd /home/<USER>/<PATH>/<TO>/internet-speedtest-pi

# activate virtualenv per source
source /home/<USER>/.cache/pypoetry/virtualenvs/<VENV>/bin/activate

# run python script
python run_speedtest.py
