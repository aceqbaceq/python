#!/bin/bash

until /home/vasya/temp/pyth1/order/order.py
do
    echo "Restarting"
    sleep 2
done
