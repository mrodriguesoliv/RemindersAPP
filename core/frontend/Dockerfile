
FROM node:14

WORKDIR /remindersapp/frontend

COPY package.json package-lock.json ./

RUN npm install

COPY . .

EXPOSE 3000

RUN npm run build

CMD ["npm", "start"]
