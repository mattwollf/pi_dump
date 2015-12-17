#!/usr/bin/env python

import spidev
import os
import MySQLdb as mdb
from time import sleep as sleep

spi = spidev.SpiDev()
spi.open(0,0)

def ReadChannel(channel):
    adc = spi.xfer2([1, (8+channel) << 4, 0])
    data = ((adc[1] &3) << 8) + adc[2]
    return data

def ConvertVolts(data, places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts, places)
    return volts

light_channel = 0

delay = 10

cnx = mdb.connect('127.0.0.1', 'root', '')

while True:
    sleep(delay)

    light_level = ReadChannel(light_channel)
    light_volts = ConvertVolts(light_level, 2)

    fout = open("light.curr", "w")
    fout.write(str(light_level))
    fout.close()
    with cnx: 
        cur = cnx.cursor()
        cur.execute("USE iotdevdb")
        cur.execute("""INSERT INTO lightlog (ldate, ltime, light, voltage) \
            VALUES( CURRENT_DATE() - INTERVAL 1 DAY, NOW(), %s, %s)""", (light_level, light_volts))

