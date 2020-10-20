#!/bin/bash
nohup redis-server > /tmp/redis.log 2>&1 &

/app/server