# pull os base image
FROM kytos_base

# set work directory

WORKDIR /
RUN mkdir -p /swagger_server
RUN mkdir -p /sdx_topology

COPY ./container-sdx-lc/swagger_server/ /swagger_server/
COPY ./container-kytos-sdx-topology/ /sdx_topology/

RUN for repo in sdx-topology/app; do cd ${repo}; python3 setup.py develop; cd ..; done
