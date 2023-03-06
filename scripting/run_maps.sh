#!/bin/sh

query='geoTwitter20-'

for file in /data/Twitter\ dataset/*
do
    zip_file=$(basename "$file")
    if echo "$zip_file" | grep -q "$query"; then
        ./src/map.py --input_path=/data/Twitter\ dataset/$zip_file
    fi
done
