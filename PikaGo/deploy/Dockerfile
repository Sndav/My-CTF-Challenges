FROM redis

COPY ./bin /app
COPY start.sh /start.sh
WORKDIR /app
RUN chmod +x /app/server
RUN chmod +x /start.sh
RUN rm -rf /app/views/menucontroller/*
RUN cat /start.sh
ENTRYPOINT [ "/start.sh" ]