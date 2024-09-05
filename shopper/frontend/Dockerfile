# pull official base image
FROM node:lts-alpine

# set working directory
WORKDIR /app

# install and cache app dependencies
COPY package*.json .
RUN npm install

# RUN npm run build

#RUN npm install react-scripts@5.0.1 -g --silent
EXPOSE 8080
# start app
CMD ["npm", "run", "serve"]
# EXPOSE 3031