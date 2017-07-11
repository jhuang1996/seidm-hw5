#!/bin/bash
sudo apt-get update
sudo pip install pip --upgrade
sudo pip install virtualenv
virtualenv -p python3 ~/.env
source ~/.env/bin/activate
xargs sudo apt-get install -y < aptlist
pip install -r requirements.txt
mysql-ctl start
mysqladmin -u root password 'root1234'
./setup_mysql.py
cd /home/ubuntu/workspace/seidm-hw5/cwb
scrapy crawl a136
cd /home/ubuntu/workspace/seidm-hw5/drf
./manage.py runserver $IP:$PORT