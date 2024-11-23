#!/bin/bash
# Script to start a Flask web server
if [ -z "$1" ]; then
    echo "Usage: $0 <python_script>"
    exit 1
fi

# Run the python script to start the server
python3 "$1"
