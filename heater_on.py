#!/usr/bin/env python

import os
import MySQLdb as mdb

import urllib2
urlstr = "http://192.168.1.10:8083/ZAutomation/api/v1/devices/ZWayVDev_zway_3-0-37/command/on"
urllib2.urlopen(urlstr)

cnx = mdb.connect('127.0.0.1', 'root', '')

with cnx:
    cur = cnx.cursor()
    cur.execute("USE iotdevdb")
    cur.execute("INSERT INTO iotlog (ldate, ltime, devname, logentry)\
        VALUES( CURRENT_DATE() - INTERVAL 1 DAY, NOW(), 'heater', 'Turned on.')")

