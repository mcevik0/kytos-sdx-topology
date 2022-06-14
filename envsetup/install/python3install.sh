cd ~
wget https://www.python.org/ftp/python/3.9.10/Python-3.9.10.tgz
tar xvf Python-3.9.10.tgz
mkdir .local
mv Python-3.9.10 .local/.
cd .local/Python-3.9.10
./configure --prefix=/home/admin/.local
sudo make clean
make
make altinstall
sudo update-alternatives --install /usr/bin/python3 python3 /home/admin/.local/bin/python3.9 1
cd ~/.local/lib/python3.9/site-packages/
ln -s /usr/share/pyshared/lsb_release.py lsb_release.py
