#!/bin/sh

pip install -r requirements.txt
python3 ./mqtt_sata_server/manage.py runserver --noreload
