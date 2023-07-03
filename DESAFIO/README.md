# Desafio Data Lake AWS - README

Este repositório contém o código e a documentação relacionados ao Desafio Data Lake AWS. O desafio consiste na criação de um Data Lake na nuvem da AWS para processar, armazenar e visualizar dados de filmes e séries com a tematica de terror.

## Observações:

Na sprint 8 o tema escolhido foi: " As tendências de lançamento do gênero terror ao longo do tempo". Com o decorrer das sprints, introdução aos tipos de modelagem e principalmente ao conceito de storytelling, o tema foi substituido na sprint 10 para: "Análise das preferências do público em relação aos subgêneros de filmes e séries de terror."

## Etapa 1: Implementação do Código Python e Carregamento no S3

Nesta etapa,  o código Python é desenvolvido para ler dois arquivos (filmes e séries) no formato CSV e utiliza a biblioteca boto3 para carregar os dados para a AWS. Os dados são gravados no S3, no bucket definido com a zona RAW, seguindo um padrão de path específico.

## Etapa 2: Criação de Container Docker e Execução Local

Na segunda etapa, criamos um container Docker com um volume para armazenar os arquivos CSV e executar o processo Python desenvolvido na Etapa 1. O objetivo é realizar a carga dos dados no S3 de forma local.

## Etapa 3: Processamento e Modelagem de Dados na Camada Trusted e Refined

Nesta etapa, dividida em duas partes, realizamos o processamento dos dados na camada Trusted do Data Lake, utilizando o Apache Spark via AWS Glue. Os dados da camada Raw são integrados e transformados em uma visão padronizada, persistida no S3 na zona Trusted em formato PARQUET. Em seguida, na camada Refined, criamos as tabelas e views no AWS Glue Data Catalog de acordo com a modelagem de dados definida, para disponibilizar os dados para a ferramenta de visualização.

## Etapa 4: Visualização de Dados com QuickSight

Na última etapa, utilizamos o QuickSight para criar painéis interativos, gráficos e relatórios com base nos dados armazenados nas camadas Trusted e Refined. Os painéis permitem que os usuários explorem os dados de forma dinâmica, identificando insights valiosos e tomando decisões estratégicas com base em informações confiáveis.

## Estrutura do Repositório

- `src/`: Contém o código Python desenvolvido para a Etapa 1.
- `docker/`: Contém os arquivos necessários para a criação do container Docker da Etapa 2.
- `spark/`: Contém os scripts e configurações para o processamento de dados nas Etapas 3 e 4.
- `docs/`: Contém a documentação relacionada ao projeto, incluindo este arquivo README e outras informações importantes.
- `data/`: Diretório para armazenar os arquivos CSV de teste.
- `visualizations/`: Diretório para armazenar imagens e recursos relacionados à visualização dos dados.

## Requisitos e Configurações

- É necessário possuir uma conta na AWS com as devidas permissões para criar e gerenciar recursos, como S3, Lambda, AWS Glue e QuickSight.
- Configurar as credenciais da conta AWS no ambiente de desenvolvimento local ou no container Docker, conforme necessário.
- O ambiente de desenvolvimento deve possuir Python, Docker e Spark instalados, além das bibliotecas requeridas pelo código Python.

## Executando o Desafio

