#!/usr/bin/env bash
# Prepare your web servers

# for install nginx
sudo apt-get update -y
sudo apt-get install nginx -y

# for create folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo sh -c 'echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"> /data/web_static/releases/test/index.html'
# for create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

# for update the Nginx conf to serve the content
sudo sh -c 'echo "server {
    listen 80;
    listen [::]:80 default_server;
    location /hbnb_static {
        alias /data/web_static/current/;
    }
}" > /etc/nginx/sites-available/default'

# for restart nginx
sudo service nginx restart
