#!/bin/bash


if [ "$#" -ne 1 ]
then
    echo "Input repository required"
    exit 1
fi

#change to your path
python3 /Users/path/to/prettify.py "$1"