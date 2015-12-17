#!/usr/bin/env python
import sys
from subprocess import call
from time import sleep

threshold = 10 
if len(sys.argv) > 1:
    threshold = sys.argv[1]
    

while True:
    fin = open("temp.curr", "r")
    heat = float(fin.read())
    fin.close()

    if(heat < threshold):

	fin = open("temp.curr", "r")
	heat = float(fin.read())
        fin.close()
        if(heat < threshold):
            call(["./heater_on.py"])
            sleep(20)
            call(["./heater_off.py"])
    
