#!/usr/bin/env bash
# This script sets up my web servers for the deployment of web_static

# Install nginx if not already installed
sudo apt -y update
sudo apt -y install nginx

# create a data directory if it doesn't already exist
# create a web_static directory if it doesn't already exist
# create a releases directory if it doesn't already exist
# create a shared directory if it doesn't already exist
# create a test directory if it doesn't already exist
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# create a fake index.html if it doesn't already exist
if [ ! -f "/data/web_static/releases/test/index.html" ];
then
    sudo bash -c 'echo "<html><head></head><body>I love you</body></html>" > /data/web_static/releases/test/index.html'
fi

# create a symbolic link, removing existing destination files
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Grant ownership of /data/ directory to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

########################################################################
# configure nginx to serve the content of /data/web_static/current/ to #
# hbnb_static using alias                                              #
########################################################################

# define path to nginx configuration file
NGINX_CONFIG="/etc/nginx/sites-available/default"

# define path to the web static content directory
CURRENT="/data/web_static/current"

# update the alias directive in the Nginx configuration
sudo sed -i "26i \\\tlocation /hbnb_static/ {\n\t\talias '$CURRENT';\n\t}\n" $NGINX_CONFIG

# start nginx to apply changes
sudo service nginx start
