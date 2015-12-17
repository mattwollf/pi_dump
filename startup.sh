#!/bin/bash

rm -f pi.pids

./status.sh ERROR

nohup ./light_logger.py &
echo $! >> pi.pids

nohup ./temp_logger.py &
echo $! >> pi.pids

nohup ./manualheattoggle.py &
echo $! >> pi.pids

nohup ./manuallighttoggle.py &
echo $! >> pi.pids

nohup ./light_control.py &
echo $! >> pi.pids

nohup ./heat_control.py &
echo $! >> pi.pids

nohup ./resetbutton.py &
echo $! >> pi.pids

./status.sh OK
