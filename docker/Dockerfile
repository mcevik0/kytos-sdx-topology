# pull os base image
FROM kytos-base

# set work directory

WORKDIR /
RUN mkdir -p /sdx_topology
COPY ./container-kytos-sdx-topology/ /sdx_topology
RUN for repo in sdx_topology/app; do cd ${repo}; python3 setup.py develop; cd ..; done
RUN touch /var/log/kytos.log
