Automate System Updates for linux systems,

first install pshh to run automation 

On Ubuntu/Debian
sudo apt-get install pssh

On CentOS/Red Hat
sudo yum install pssh

add ip addresses for systems to hosts.txt

Run command

pssh -h hosts.txt -l username -i "python automate_updates.py"
