#!/bin/bash

#import connectVirtualEnv function
source ./connect.sh

sudo apt install -y python3-venv
python3 -m venv .venv
connectVirtualEnv

if [ -f requirements.txt ]; then
    pip install -r requirements.txt
else
    pip freeze > requirements.txt
    echo "requirements.txt not found, skipping installation of dependencies."
fi