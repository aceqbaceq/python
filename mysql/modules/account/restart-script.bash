#!/bin/bash

until ./main.py
do
    echo "Restarting"
    sleep 2
done

