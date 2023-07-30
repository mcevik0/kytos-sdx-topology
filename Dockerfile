# pull os base image
FROM kytos-base

# set work directory

WORKDIR /
RUN mkdir -p /swagger_server
RUN mkdir -p /sdx_topology
COPY ./container-sdx-lc/sdx-lc/swagger_server /swagger_server
COPY ./container-sdx-lc/curl /curl
COPY ./container-sdx-lc/curl/gunicorn.sh .
COPY ./container-kytos-sdx-topology/ /sdx_topology
RUN for repo in sdx_topology/app; do cd ${repo}; python3 setup.py develop; cd ..; done
