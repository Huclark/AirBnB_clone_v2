#!/usr/bin/env bash
# This script sets up my web servers for the deployment of web_static

# Install nginx if not already installed
if ! service nginx status &> /dev/null; then
    sudo apt -y update
    sudo apt -y install nginx
    sudo service nginx start
fi

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
sudo chown -hR ubuntu:ubuntu /data/

########################################################################
# configure nginx to serve the content of /data/web_static/current/ to #
# hbnb_static using alias                                              #
########################################################################

# update the alias directive in the Nginx configuration
sudo sed -i "s,server_name _;,server_name _;\n\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n,g" /etc/nginx/sites-available/default

# start nginx to apply changes
sudo service nginx start
