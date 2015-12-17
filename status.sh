#!/bin/bash

ESTR="ERROR"
OKSTR="OK"

GREENLIGHT=20
REDLIGHT=21

gpio -g mode $GREENLIGHT out
gpio -g mode $REDLIGHT out

if [ "$ESTR" == "$1" ]
then
    gpio -g write $GREENLIGHT 0
    gpio -g write $REDLIGHT 1
    ./logerror.py
fi

if [ "$OKSTR" == "$1" ]
then
    gpio -g write $REDLIGHT 0
    gpio -g write $GREENLIGHT 1
    ./logok.py
fi
