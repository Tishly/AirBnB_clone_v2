#!/usr/bin/env bash
# Ascript to setup the static env

apt-get update
apt-get install -y nginx
mkdir -p /data/web_static/releases/
mkdir -p data/web_static/shared/
mkdir -p /data/web_static/releases/test/index.html
mkdir -p

