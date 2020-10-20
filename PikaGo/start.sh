#!/bin/sh
/usr/bin/supervisord
supervisorctl -c /etc/supervisord.conf start server
while true; do
    supervisorctl -c /etc/supervisord.conf restart server 
    rm -rf /app/views/menucontroller/*
    sleep 20; 
done