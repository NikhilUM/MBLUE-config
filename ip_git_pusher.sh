#!/bin/bash 

HOSTNAME=$(hostname -f)

cd /etc/MBLUE-config
git pull origin main
python ip_yaml_editor.py
git add -A
git commit -a -m "Updated IP address: $HOSTNAME"
git push origin main
