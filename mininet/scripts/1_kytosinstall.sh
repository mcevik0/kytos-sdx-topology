#!/bin/sh
sudo rm -r kytos
sudo rm -r /var/lib/kytos
sudo rm -r /var/run/kytos
sudo rm -r /var/tmp/kytos
sudo rm -r /etc/kytos
sudo mkdir /var/lib/kytos
sudo mkdir /var/run/kytos
sudo mkdir /var/tmp/kytos
sudo mkdir /etc/kytos
sudo chown -R admin:admin /var/lib/kytos
sudo chown -R admin:admin /var/run/kytos
sudo chown -R admin:admin /var/tmp/kytos
sudo chown -R admin:admin /etc/kytos
mkdir /home/admin/kytos
cp /home/admin/install/4_clone_kytos.sh /home/admin/kytos/.
cp /home/admin/install/5_install_kytos.sh /home/admin/kytos/.
echo Remember to activate the environment: source python-kytos/bin/activate 
