#!/bin/bash 

HOSTNAME=$(hostname -f)

cd /home/pi/MBLUE-config
git pull origin main

python /home/pi/MBLUE/utilities/ip_yaml_editor.py

cd /home/pi/MBLUE-config
git add -A
git commit -a -m "Updated IP address: $HOSTNAME"
git push origin main