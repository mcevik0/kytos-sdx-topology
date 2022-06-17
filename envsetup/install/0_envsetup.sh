sudo apt-get update
sudo apt-get upgrade
sudo apt-get install 
apt-get install --assume-yes --no-install-recommends \
	build-essential \
       	ca-certificates
       	curl \
	dirmngr \
	docker-ce \
	docker-ce-cli \
	containerd.io \
	docker-compose-plugin \
	dpkg-dev \
	gcc \
	git \
	gnupg \
	gunicorn \
	iputils-ping \
	libbz2-dev \
	libc6-dev \
	libexpat1-dev \
	libffi-dev \
	liblzma-dev \
	libncurses5-dev \
	libgdbm-dev \
	libnss3-dev \
	libreadline-dev \
	libsqlite3-dev \
	libssl-dev \
       	lsb-release \
	lsof \
	make \
	mininet \
	netbase \
	netcat \
	python3-venv \
	software-properties-common \
	uuid-dev \
	wget \
	xz-utils \
	zlib1g-dev
cd ~
# wget https://www.python.org/ftp/python/3.9.10/Python-3.9.10.tgz
tar xvf Python-3.9.10.tgz
mkdir .local
mv Python-3.9.10 .local/.
cd .local/Python-3.9.10
./configure --prefix=/home/admin/.local
sudo make clean
sudo make
sudo make altinstall
sudo update-alternatives --install /usr/bin/python3 python3 /home/admin/.local/bin/python3.9 1
cd ~/.local/lib/python3.9/site-packages/
ln -s /usr/share/pyshared/lsb_release.py /usr/local/lib/python3.9/site-packages/lsb_release.py

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
sudo apt update
sudo apt-get install gnupg2
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/5.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
sudo apt update
sudo apt-get install -y mongodb-org-shell


sudo apt install python3-pip
sudo apt install python3-ven
sudo ln -s /usr/local/bin/pip3.9 /usr/local/bin/pip3
sudo ln -s /usr/local/bin/pip3.9 /usr/local/bin/pip
pip3 install --upgrade pip
