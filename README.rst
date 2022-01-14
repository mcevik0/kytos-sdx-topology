Overview
========
SDX API

Kytos Napp to handle the requirements of the AtlanticWave-SDX project.

Requirements
============

* kytos/core
* kytos/topology
* kytos/storehouse
* openAPI Specification
* swagger client
* flask
* python 3.7

Preparing the environment:
==========================

``Installing Python``

If you don't have Python 3 installed, please install it. Please make sure that you're using python3.6
or a later version::

$ apt install python3

``Installing Docker & Kytos``

Then, create a docker container to contain all your work. To download a docker image with kytos pre-installed run: ::

$ docker pull kytos/nightly:latest
$ docker run -d --name kytos -p 6653:6653 -p 8181:8181 --privileged kytos/nightly:latest /usr/bin/tail -f /dev/null

Now, access a shell session inside your container::

$ docker exec -it kytos bash

Make sure kytos is running::

$ kytosd -E # run kytos in the background

or ::

$ kytosd -E -f # run kytos in the foreground

``Installing Mininet``

Download VirtualBox and install Mininet. Then to set-up your network, run the following::

$ mn --topo linear,3 --controller=remote,ip=,port=6653



Downloading the SDX Kytos Napp
================================


All of the Kytos Network Applications are located in the NApps online repository. To install the SDX NApp, run the
following from inside the docker container::

$ kytos napps install amlight/sdx

Or we can clone directly from the Amlight Github repository via git::

$ git clone https://github.com/amlight/amlight-sdx.git
$ cd amlight-sdx
$ python3 setup.py develop


Installing swagger_client
==========================

For the whole installation process and requirements, please access
the AtlanticWave SDX repo in Github: https://github.com/atlanticwave-sdx

How to Use
==========

TBD


Version
=======

1.0.0

