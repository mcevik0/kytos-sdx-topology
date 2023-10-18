#!/bin/sh
cmd="tail -f /var/log/kytos.log"
docker exec -it amlight $cmd
