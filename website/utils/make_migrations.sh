#!/usr/bin/env bash

python3 ../manage.py makemigrations
python3 ../manage.py migrate
python3 ../manage.py collectstatic
mysql -u root ndm < ./node.sql
mysql -u root ndm < ./node_connect.sql
mysql -u root ndm < ./device_group.sql
mysql -u root ndm < ./device_type.sql
mysql -u root ndm < ./device.sql