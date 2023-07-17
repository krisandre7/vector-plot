# syntax=docker/dockerfile:1

FROM mysql:8.0.33

# Mantenedor
LABEL version="1.0"
LABEL author="Kristhian Aguilar (kris.andre7@gmail.com)"
LABEL description="Teste"

ENV MYSQL_ROOT_PASSWORD=root \
    MYSQL_USER=prometheus \
    MYSQL_PASSWORD=12345 \
    MYSQL_DATABASE=data_vector

ADD data_vector.sql /docker-entrypoint-initdb.d

EXPOSE 3306