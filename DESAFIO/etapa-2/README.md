### ETAPA 1 DO DESAFIO. ###

# Integração do AWS Lambda com a API do TMDB #

Na segunda etapa deste desafio, focaremos na integração do AWS Lambda com a API do The Movie Database (TMDB) para complementar os dados de análise. O objetivo é buscar informações adicionais sobre os filmes e séries a partir da API do TMDB e, em seguida, gravar esses dados no Amazon S3 usando a biblioteca boto3.

## Parte 1: Criação de Nova Camada (Layer) no AWS Lambda

Primeiramente, criaremos uma nova camada (layer) no serviço AWS Lambda. Essa camada conterá as bibliotecas necessárias para a ingestão de dados, como, por exemplo, a biblioteca para interação com a API do TMDB. Essa camada será utilizada pelo código Python do AWS Lambda, facilitando o gerenciamento de dependências.

## Parte 2: Implementação do AWS Lambda para Consumo de Dados do TMDB

Nesta etapa, desenvolveremos o código Python para o AWS Lambda, que consumirá dados da API do TMDB. Utilizando a biblioteca integrada à camada criada na Parte 1, faremos requisições à API do TMDB para obter informações adicionais sobre os filmes e séries.

Após a obtenção desses dados, utilizaremos a biblioteca boto3 para gravá-los no Amazon S3. Os arquivos serão armazenados seguindo o padrão de path definido, contendo o nome do bucket, a camada de armazenamento, a origem e formato dos dados, a especificação do dado e a data de processamento, separada por ano, mês e dia.

Exemplos de caminhos de arquivos válidos no S3:
```
S3:\\data-lake-do-fulano\Raw\TMDB\JSON\2022\05\02\prt-uty-nfd.json
S3:\\data-lake-do-fulano\Raw\Twitter\JSON\2022\05\02\idf-uet-wqt.json
```

## Parte 3: Teste e Validação do AWS Lambda

Após a implementação, realizaremos testes e validações do AWS Lambda em nossa conta AWS. Verificaremos se o código Python consegue consumir corretamente os dados do TMDB e realizar a gravação no Amazon S3 seguindo o padrão de path estabelecido.

A integração do AWS Lambda com a API do TMDB será fundamental para enriquecer o conjunto de dados de filmes e séries armazenados em nosso Data Lake na AWS. A capacidade de buscar informações adicionais a partir de uma fonte externa ampliará as possibilidades de análise e insights que poderemos obter a partir dos dados.

---

