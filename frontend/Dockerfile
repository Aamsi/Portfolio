FROM node:10

WORKDIR /frontend/

COPY . /frontend

RUN npm install

EXPOSE 8080

CMD ["npm", "run", "serve"]