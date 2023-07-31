#!/bin/sh

lsof -i -P -n | grep LISTEN
netstat -tulpn | grep LISTEN
ss -tulpn | grep LISTEN
lsof -i:8080
sudo nmap -sTU -O 192.168.0.2
