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
Antes de executar o programa, é necessário subir o container Docker do banco de dados My SQL a partir da imagem no Dockerfile. Para isso, crie a imagem dentro da pasta docker, através do script:

```
sudo chmod 777 create_image.sh
./create_image.sh
```

Depois, conceda permissões ao script run_container.sh e depois o execute:

```
sudo chmod 777 run_container.sh
./run_container.sh
```
Se não quiser usar o script, use os seguintes comandos para iniciar o container:
```
cd docker
docker build -t mysql-vector .
cd ..
docker run --name mysql-python -p 3306:3306 -d mysql-vector
```
Para executar o programa, navegue até a pasta vector plot e execute main.py
```
python main.py
```

