# Developed By Sndav

FROM ubuntu:16.04

ENV LANG C.UTF-8
RUN sed -i 's/archive.ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list
RUN sed -i 's/security.ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list
RUN apt-get update

RUN apt-get -y install apache2
RUN apt-get install php7.0-fpm php7.0-mysql php7.0-common php7.0-mbstring php7.0-gd php7.0-json php7.0-cli php7.0-curl libapache2-mod-php7.0 -yqq

RUN rm -f /var/www/html/index.html
RUN mkdir /var/www/html/sandbox/
RUN chmod 777 -R /var/www/html/sandbox/

ADD ./start.sh /start.sh
RUN chmod +x /start.sh

ENTRYPOINT [ "/start.sh" ]
