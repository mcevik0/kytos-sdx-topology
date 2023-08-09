#!/bin/sh
cmd="tail -f /var/log/amlight/access_validator.log"
docker exec -it amlight $cmd
