#!/bin/bash
#Subir o ambiente do Banco de Dados Relacional MySQL
result_mysql=$(docker container ls -a | grep mysql-python)
container_mysql='mysql-python'

# verificar se o container mysql-python já foi criado
if [[ "$result_mysql" == *"$container_mysql"* ]]
then
    # apenas inicializa o container caso já esteja criado
    docker container start mysql-python
else
    # cria o container caso não foi criado
    docker run --name mysql-python  -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_USER=prometheus -e MYSQL_PASSWORD=12345 -e MYSQL_DATABASE=data_vector -d mysql:8.0.33
fi

# docker stop mysql-python

# # --name    nome do container
# # -v        mapear volume local:dentro_container
# # -it       modo iterativo, ou seja, permite entrar no container em modo console
# # -p        externalizar uma porta para acesso internamente ao container

# docker container stop mysql-python

# rm -f     apaga um container (-f )

# Fonte: https://docs.docker.com/engine/reference/run/