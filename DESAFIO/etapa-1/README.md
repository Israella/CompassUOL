### ETAPA 1 DO DESAFIO. ###

## Desafio de Carga de Dados para a AWS##

Este repositório contém a implementação de um desafio que consiste em carregar arquivos CSV de filmes e séries para a Amazon Web Services (AWS). O objetivo é utilizar a biblioteca boto3 do Python para transferir os dados para o serviço de armazenamento S3 da AWS.

## Parte 1: Implementação do Código Python

Na primeira parte deste desafio, implementamos um código Python para ler os arquivos CSV completos de filmes e séries, sem filtrar os dados. Em seguida, utilizamos a biblioteca boto3 para estabelecer conexão com a AWS e realizar a gravação dos dados no S3.

Os arquivos são armazenados seguindo um padrão específico no S3, que inclui o nome do bucket, a camada de armazenamento, a origem e formato dos dados, a especificação do dado e a data de processamento, separada por ano, mês e dia.

Exemplo de caminho do arquivo no S3:
```
S3:\\data-lake-do-fulano\Raw\Local\CSV\Movies\2022\05\02\movies.csv
S3:\\data-lake-do-fulano\Raw\Local\CSV\Series\2022\05\02\series.csv
```

## Parte 2: Criação do Container Docker

Na segunda parte do desafio, criamos um container Docker que incorpora o código Python desenvolvido na Parte 1. Além disso, configuramos um volume dentro do container para armazenar os arquivos CSV.

O uso do container Docker permite a execução do processo de carga de dados de maneira isolada e replicável em diferentes ambientes.

## Parte 3: Execução Local do Container Docker

Para realizar a carga dos dados no S3 da AWS, executamos localmente o container Docker criado na Parte 2. Essa execução local nos permite testar e validar o processo de carga antes de implantá-lo em um ambiente de produção.

Neste desafio, aprendemos a trabalhar com a biblioteca boto3 para interagir com a AWS, criamos um container Docker com volume para facilitar o transporte dos arquivos CSV e executamos o processo de carga localmente.

O resultado final é a eficiente transferência dos dados de filmes e séries para a AWS, tornando-os disponíveis para uso em um ambiente de Data Lake ou análise de dados.

---
