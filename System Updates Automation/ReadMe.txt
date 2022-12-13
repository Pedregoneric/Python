Automate System Updates for linux systems,

first install pshh to run automation 

On Ubuntu/Debian
sudo apt-get install pssh
sudo apt-get install parallel-ssh

On CentOS/Red Hat
sudo yum install pssh

Install Subprocess module to run process via python
sudo apt-get install python-pip
pip install subprocess

if errors, download manually using following steps:

1. wget https://files.pythonhosted.org/packages/89/23/d0e9f0c9274a9959a1bbf50a7e8e0c88e7b5f1b95ab7b946d6c3b3e3a47a/subprocess32-3.5.4.tar.gz
2. tar -xzf subprocess32-3.5.4.tar.gz
3. cd subprocess32-3.5.4
4. python setup.py install

add ip addresses for systems to hosts.txt

Run command

parallel-ssh hosts username "update systems python.py"
or
pssh -h hosts.txt -l username -i "update systems python"
