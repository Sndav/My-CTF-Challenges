FROM node
COPY src /app
WORKDIR /app
RUN npm --registry https://registry.npm.taobao.org install
ENTRYPOINT [ "node","/app/app.js" ]