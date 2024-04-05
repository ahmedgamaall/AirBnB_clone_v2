#!/usr/bin/env bash
sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo sh -c 'echo "this is Emad"> /data/web_static/releases/test/index.html'
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sh -c 'echo "server {
    listen 80;
    listen [::]:80 default_server;
    server_name 52.3.243.117;
    location /hbnb_static {
        alias /data/web_static/current/;
    }
}" > /etc/nginx/sites-available/default'
sudo service nginx restart
