#!/usr/bin/env bash
set -e

docker exec -it $(docker-compose ps -q backend) bash
