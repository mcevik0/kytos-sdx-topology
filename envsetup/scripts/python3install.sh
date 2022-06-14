sudo apt-get install wget build-essential libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev liblzma-dev -y
wget https://www.python.org/ftp/python/3.9.10/Python-3.9.10.tgz
tar xzf Python-3.9.10.tgz
cd Python-3.9.10 && ./configure --enable-optimizations
# make altinstall

