#!/usr/bin/env python

import os
import MySQLdb as mdb
from time import sleep as sleep
import RPi.GPIO as GPIO
from subprocess import call

GPIO.setmode(GPIO.BCM)

BUTTON=16

GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)


state = 0

def toggleheat():
    global state
    if state == 0:
        state = 1
        call(["./heater_on.py"])
    elif state == 1:
        state = 0
        call(["./heater_off.py"])
        

while True:

    input_state=GPIO.input(BUTTON)

    if input_state == False:
        #button is pressed
        toggleheat()
        sleep(5)
	
