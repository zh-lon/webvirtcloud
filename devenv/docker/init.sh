#!/usr/bin/env bash
set -e

echo
echo "Building docker images..."

docker-compose up -d
echo "Building docker images... OK"

echo
echo "Setup environment..."

# Waiting containers
sleep 60

# MariadDB
docker exec -it $(docker-compose ps -q mariadb) \
       mysql -uroot -proot -e "CREATE DATABASE webvirtcloud CHARACTER SET utf8 COLLATE utf8_general_ci"

# Django migrations
docker exec -it $(docker-compose ps -q backend) python3.6 manage.py migrate
docker exec -it $(docker-compose ps -q backend) python3.6 manage.py migrate --database=powerdns
docker exec -it $(docker-compose ps -q backend) python3.6 manage.py loaddata */fixtures/*

echo
echo "Setup environment... OK"
echo