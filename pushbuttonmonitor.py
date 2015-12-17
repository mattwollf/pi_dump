#!/usr/bin/env python

import os
import MySQLdb as mdb
from time import sleep as sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

BUTTON=16

GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)


cnx = mdb.connect('127.0.0.1', 'root', '')

while True:

    input_state=GPIO.input(BUTTON)

    if input_state == False:
        print "button pressed"

    with cnx: 
        cur = cnx.cursor()
        #cur.execute("USE iotdevdb")

