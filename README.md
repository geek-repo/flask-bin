# flask-bin
# As for the Database I have used ElasticSearch on docker 

# Usage:- 
---tmux recommended----
python3 server.py
python3 remover.py

# Installation for ElasticSearch
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.6.2.deb

dpkg -i elasticsearch-6.6.2.deb

apt install -f

systemctl start elasticsearch.service

pip3 install -r requirements.txt

curl http://localhost:9200/
----------------------------------------------------
It is the light weight service which works like pastebin 

# Test Site :- http://weebsec.com:1337/

![](ezgif-4-ec4f4e005dda.gif)
