#!/usr/bin/env python

import os
import MySQLdb as mdb
from time import sleep as sleep
import RPi.GPIO as GPIO
from subprocess import call

GPIO.setmode(GPIO.BCM)

BUTTON=23

GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:

    input_state=GPIO.input(BUTTON)

    if input_state == False:
        call(["./reset.sh"])

