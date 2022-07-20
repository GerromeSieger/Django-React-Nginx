FROM node:16.13.1-alpine as builder

WORKDIR /react

COPY package.json .

RUN npm install -g npm@8.14.0

RUN npm install

COPY . .

RUN npm run build
#CMD ["npm","start"]



#FROM nginx:1.19.0-alpine

#COPY --from=builder /react/build /usr/share/nginx/html

#COPY nginx-setup.conf /etc/nginx/conf.d/default.conf

#CMD ["nginx","-g","daemon off;"]
