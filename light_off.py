#!/usr/bin/env python

import urllib2
import md5
import os
from time import sleep
import MySQLdb as mdb

urlstr = "http://192.168.1.10:8083/ZAutomation/api/v1/devices/ZWayVDev_zway_2-0-38/command/off"
urllib2.urlopen(urlstr)

cnx = mdb.connect('127.0.0.1', 'root', '');

with cnx:
    cur = cnx.cursor()
    cur.execute("USE iotdevdb")
    cur.execute("INSERT INTO iotlog (ldate, ltime, devname, logentry) \
        VALUES( CURRENT_DATE() - INTERVAL 1 DAY, NOW(), 'heater', 'Turned off.')")
