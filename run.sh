#!/bin/sh

pip install -r requirements.txt
python3 ./mqtt_data_server/manage.py runserver --noreload
