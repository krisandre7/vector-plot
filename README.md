# vector-plot
Script Python para realizar limpeza e plotagem de vetores tridimensionais, hospedados em um container MySQL.

## Pré-Requisitos
É necessário instalar todas as dependências contidas no arquivo requirements.txt para a execução do programa. Isso pode ser feito tanto pelo PIP quanto pelo Conda:
```
pip install -r requirements.txt
OU
conda list -e > requirements.txt
```
Também é necessário ter Docker instalado.

## Uso
Antes de executar o programa, é necessário subir o container Docker do banco de dados My SQL. Para isso, conceda permissões ao script run_container.sh e depois o execute:

```
sudo chmod 777 run_container.sh
./run_container.sh
```
Se não quiser usar o script, use o seguinte comando para iniciar o container:
```
docker run --name mysql-python  -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_USER=prometheus -e MYSQL_PASSWORD=12345 -e MYSQL_DATABASE=data_vector -d mysql:8.0.33
```

Após isso, será necessário carregar as coordenadas dos vetores e magnitudes no banco de dados. Isso pode ser feito ao se executar o arquivo "data_vector.sql" na base de dados, utilizando uma aplicação como MySQL Workbench.

Para executar o programa, navegue até a pasta vector plot e execute main.py

```
python main.py
```

