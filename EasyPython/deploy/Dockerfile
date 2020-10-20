FROM python:2.7

RUN sed -i 's/deb.debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list
RUN sed -i 's/security.debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list

RUN printf '#!/bin/sh\nexit 0' > /usr/sbin/policy-rc.d
RUN apt update -y
RUN apt -y install supervisor gcc
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple gunicorn gevent flask supervisor

COPY src /app
COPY readflag.c /readflag.c
COPY start.sh /start.sh

WORKDIR /
RUN mkdir /home/supervisor
RUN chmod +x /start.sh
RUN gcc readflag.c -o readflag
RUN chmod u+s /readflag
RUN chmod 644 /app/app.py
RUN chmod 644 /app/wsgi.py
RUN useradd ctf

ENTRYPOINT [ "/start.sh" ]
