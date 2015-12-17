#!/usr/bin/env python

import os
import MySQLdb as mdb
from time import sleep as sleep
import RPi.GPIO as GPIO
from subprocess import call

GPIO.setmode(GPIO.BCM)

BUTTON=12

GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

state = 0

def togglelights():
    global state
    if state == 0:
        state = 10
        call(["./light_on.py"])
    elif state == 1:
        state = 0
        call(["./light_off.py"])
    else:
        state += 10
        call(["./light_set.py", str(state)])
        if state > 100:
           state = 1

while True:

    input_state=GPIO.input(BUTTON)

    if input_state == False:
        print state
        sleep(0.5)
        togglelights()
