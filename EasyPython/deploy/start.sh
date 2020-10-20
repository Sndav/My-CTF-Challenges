#!/bin/sh
nohup redis-server > /tmp/redis.log 2>&1 &
/usr/bin/supervisord -c /etc/supervisord.conf
supervisorctl -c /etc/supervisord.conf start gunicorn
while true; do
    supervisorctl -c /etc/supervisord.conf restart gunicorn 
    sleep 20; 
done