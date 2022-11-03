#!/usr/bin/env bash

if [[ ! -d /data/web_static/ ]]
then
	mkdir /data/web_static/releases/test && /data/web_static/shared/
fi

if [[ ! -f /data/web_static/current ]]
then
	touch /data/web_static/current
fi

if [[ ! -f /data/web_static/releases/test/index.html ]]
then
	touch /data/web_static/releases/test/index.html
	echo "<!DOCTYPE html>
	<html>
	<body>
	  <h1>Eka's Corner</h1>
	  </body>
	  </html>" > index.html
fi

sudo ln -s /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
echo "" >> /etc/nginx/nginx.conf
