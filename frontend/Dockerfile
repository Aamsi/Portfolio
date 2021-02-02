FROM node:10

WORKDIR /frontend/

COPY . /frontend

RUN yarn

EXPOSE 8080
CMD ["yarn", "run", "serve"]