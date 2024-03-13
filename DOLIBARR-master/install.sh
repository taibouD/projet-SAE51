#!/bin/bash

# Créer un fichier docker-compose.yml
echo "version: '3'
volumes:
  dolibarr_html:
  dolibarr_docs:
  dolibarr_db:

services:

  mariadb:
    image: mariadb:latest
    container_name: mariadb
    restart: unless-stopped
    command: --character_set_client=utf8 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
    volumes:
      - dolibarr_db:/var/lib/mysql
    environment:
      - MYSQL_DATABASE=dolibarr
      - MYSQL_USER=dolibarr
      - MYSQL_PASSWORD=dolibarr
      - MYSQL_ROOT_PASSWORD=foo

  dolibarr:
    image: upshift/dolibarr:latest
    container_name: dolibarr
    restart: unless-stopped
    depends_on:
      - mariadb
    ports:
      - "9000:80"
    environment:
      - DOLI_ADMIN_LOGIN=admin
      - DOLI_ADMIN_PASSWORD=mypass
      - DOLI_DB_HOST=mariadb
      - DOLI_DB_NAME=dolibarr
      - DOLI_DB_USER=dolibarr
      - DOLI_DB_PASSWORD=dolibarr
      - TZ=Europe/Paris
    volumes:
      - dolibarr_html:/var/www/html
      - dolibarr_docs:/var/www/documents

  phpmyadmin:
    image: phpmyadmin/phpmyadmin:latest
    container_name: phpmyadmin
    restart: unless-stopped
    depends_on:
      - mariadb
    environment:
      - PMA_HOST=mariadb
      - PMA_USER=dolibarr
      - PMA_PASSWORD=dolibarr
    ports:
      - "8080:80"
" > docker-compose.yml

# Lancer Docker Compose
docker-compose up -d

echo "Dolibarr et le SGBD ont été installés avec succès."

