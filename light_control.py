#!/usr/bin/env python
import sys
from subprocess import call
from time import sleep

threshold = 600 
if len(sys.argv) > 1:
    threshold = sys.argv[1]
    
intensity = 0

while True:
    fin = open("light.curr", "r")
    light = int(fin.read())

    if(light > threshold):
        sleep(5)

        if intensity > 80:
            call(["./light_on.py"])
        else:
            intensity += 10
            call(["./light_set.py", str(intensity)])

    
