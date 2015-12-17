#!/usr/bin/env python

import MySQLdb as mdb
from time import sleep as sleep

cnx = mdb.connect('127.0.0.1', 'root', '')

with cnx:
    cur = cnx.cursor()
    cur.execute("USE iotdevdb")
    cur.execute("""INSERT INTO iotlog (ldate, ltime, devname, logentry) \
        VALUES(CURRENT_DATE() - INTERVAL 1 DAY, NOW(), 'pi', 'ENTERED OK STATE')""")

