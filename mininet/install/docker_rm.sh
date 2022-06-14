#!/bin/sh
sudo docker system prune --all --volumes

# Remove all containers that aren't running.
sudo docker rm -vf $(docker ps -a -q --filter "status=exited")

# Remove untagged images.
sudo docker rmi -f $(docker images -q -f "dangling=true")

# Remove unused volumes using "rm" or "prune".
sudo docker volume rm -f $(docker volume ls -f "dangling=true")
sudo docker volume prune -f

# Remove unused networks.
sudo docker network prune -f

# Display running containers.
docker ps

# Display all containers using "-a" or "--all".
docker ps -a
docker ps --all

# Filter output using "-f" or "--filter".
docker ps -f "status=exited"
docker ps --filter "status=exited"

# Show only the container ID using "-q" or "--quiet".
docker ps -q -f "status=exited"
docker ps --quiet --filter "status=exited"

# Remove an individual container by ID or name.
# Use "-v" or "--volumes" to remove associated volumes.
# Use "-f" or "--force" to remove running containers.
#docker rm -vf b0479f9d1ea4
#docker rm --volumes --force ol7_ords_con

# Remove all the containers matching the "ps" output.
sudo docker rm -vf $(docker ps -a -q --filter "status=exited")

# Show top-level images only.
docker images

# Show all images using "-a" or "--all".
docker images -a
docker images --all

# Filter the output using "-f" or "--filter".
docker images -f "dangling=true"
docker images --filter "dangling=true"

# Display only the image ID using "-q" or "--quiet".
docker images -q -f "dangling=true"
docker images --quiet --filter "dangling=true"

# Remove image by image ID or repository:tag
#docker rmi ffcd22192b23
#docker rmi ol7_122:latest

# Force the remove using "-f" or "--force".
#docker rmi -f ffcd22192b23
#docker rmi --force ol7_122:latest

# Remove images matching list.
sudo docker rmi -f $(docker images -q -f "dangling=true")

# List all volumes.
docker volume ls

# Filter output using "-f" or "--filter".
docker volume ls -f "dangling=true"
docker volume ls --filter "driver=local"

# Display only volume name using "-q" or "--quiet".
docker volume ls -q -f "driver=local"
docker volume ls --quiet --filter "driver=local"

# Remove specified volume.
#docker volume rm test_vol

# Force removal using "-f" or "--force".
#docker volume rm -f test_vol
#docker volume rm --force test_vol

# Remove unused volumes.
sudo docker volume rm -f $(docker volume ls -f "dangling=true")

# Remove unused volumes.
sudo docker volume prune -f

# List all networks.
docker network ls

# Filter output using "-f" or "--filter".
docker network ls -f "driver=bridge"
docker network ls --filter "driver=bridge"

# Display only network ID using "-q" or "--quiet".
docker network ls -q -f "driver=bridge"
docker network ls --quiet --filter "driver=bridge"

# Remove network by name or ID.
#docker network rm my_network2
#docker network rm 6466079abd47

# Remove unused networks.
sudo docker network prune

# Force prune  using "-f" or "--force".
sudo docker network prune -f
sudo docker network prune --force

