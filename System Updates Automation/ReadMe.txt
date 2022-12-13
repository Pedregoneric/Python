Automate System Updates for linux systems,

first install pshh to run automation 

On Ubuntu/Debian
sudo apt-get install pssh
sudo apt-get install parallel-ssh

On CentOS/Red Hat
sudo yum install pssh

add ip addresses for systems to hosts.txt

Run command

parallel-ssh hosts username "update systems python.py"
or
pssh -h hosts.txt -l username -i "update systems python"
