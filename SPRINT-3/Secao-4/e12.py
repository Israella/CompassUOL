#Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

import json

# Lê o conteúdo do arquivo JSON
with open('person.json', 'r') as arquivo:
    conteudo = arquivo.read()

# Faz o parsing do conteúdo JSON para um dicionário Python
dados = json.loads(conteudo)

# Imprime o conteúdo do dicionário
print(dados)