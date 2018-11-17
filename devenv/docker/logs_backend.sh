#!/usr/bin/env bash
set -e

docker logs -f $(docker-compose ps -q backend)

