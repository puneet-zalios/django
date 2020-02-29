#!/bin/bash

docker-compose -f docker-compose.yml build --pull
docker-compose -f docker-compose.yml up -d --remove-orphans
