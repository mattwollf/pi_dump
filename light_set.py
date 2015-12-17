#!/usr/bin/env python

import os
import MySQLdb as mdb
import sys;

import urllib2

value = 99
if len(sys.argv) > 1:
    value = int(sys.argv[1])
    

urlstr = """http://192.168.1.10:8083/ZAutomation/api/v1/devices/ZWayVDev_zway_2-0-38/command/exact?level=""" + str(value)

urllib2.urlopen(urlstr)

cnx = mdb.connect('127.0.0.1', 'root', '')

with cnx:
    cur = cnx.cursor()
    cur.execute("USE iotdevdb")
    cur.execute("""INSERT INTO iotlog (ldate, ltime, devname, logentry)\
        VALUES( CURRENT_DATE() , NOW(), 'light', 'Dimmed to %s')""",(value))
