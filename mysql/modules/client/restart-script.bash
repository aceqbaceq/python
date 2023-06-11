#!/bin/bash

until ./main-loop.py
do
    echo "Restarting"
    sleep 2
done

