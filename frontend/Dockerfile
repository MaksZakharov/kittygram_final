FROM node:18 AS build

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY . .
RUN npm run build

# ------------------------
# production stage
FROM nginx:1.22.1

# Копируем билд React в стандартное место для Nginx
COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

COPY nginx.conf /etc/nginx/conf.d/default.conf
