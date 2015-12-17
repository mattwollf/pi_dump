#!/bin/bash

./status.sh ERROR

while read line; do
    echo KILLING PID $line
    kill $line
done < pi.pids

./heater_off.py
./light_off.py

./startup.sh

