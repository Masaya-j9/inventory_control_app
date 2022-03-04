FROM node:latest

ENV LANG=C.UTF-8
ENV TZ=Asia/Tokyo
ENV APP=/app/

RUN mkdir -p ${APP}
WORKDIR ${APP}

COPY package.json ${APP}

COPY package-lock.json ${APP}

RUN npm install -g ts-node
RUN npm install -g typescript
RUN npm install -g react-scripts

RUN npm install

COPY . ${APP}

EXPOSE 3000

ENTRYPOINT [ "npm" ]

CMD ["start"]
