#!/usr/bin/env python

import spidev
import os
import MySQLdb as mdb
from time import sleep as sleep

#spi bus

spi = spidev.SpiDev()
spi.open(0,0)

def ReadChannel(channel):
    adc = spi.xfer2([1, (8+channel) << 4, 0])
    data = ((adc[1] &3) << 8) + adc[2]
    return data

def ConvertVolts(data, places):
    volts = (data * 3.3) / float(1023)
    volta = round(volts, places)
    return volts

def ConvertTemp(data, places):
    temp = ((data * 330) / float(1023)) - 50
    temp = round(temp, places)
    return temp

temp_channel = 1

delay = 10

cnx = mdb.connect('127.0.0.1', 'root', '')
while True:

    sleep(delay)
    temp_level = ReadChannel(temp_channel)
    temp_volts = ConvertVolts(temp_level, 2)
    temp = ConvertTemp(temp_level, 2)

    fout = open("temp.curr", "w")
    fout.write(str(temp))
    fout.close()

    with cnx:
        cur = cnx.cursor()
        cur.execute("USE iotdevdb")
        cur.execute("""INSERT INTO templog (ldate, ltime, temperature, voltage) \
            VALUES( CURRENT_DATE() - INTERVAL 1 DAY, NOW(), %s, %s)""", (temp, temp_volts))
