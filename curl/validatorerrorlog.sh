#!/bin/sh
cmd="tail -f /var/log/amlight/error_validator.log"
docker exec -it amlight $cmd
