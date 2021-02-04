FROM node:12

WORKDIR /frontend/

COPY . /frontend

RUN yarn

EXPOSE 8080

CMD ["yarn", "serve"]