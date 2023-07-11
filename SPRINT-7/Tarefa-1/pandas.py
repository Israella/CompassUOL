import pandas as pd
import numpy as np

# Leitura do arquivo CSV usando pandas
df = pd.read_csv('actors.csv')

# Tarefa 1: Identificar o ator/atriz com maior número de filmes e o respectivo número de filmes
maior_num_filmes = df['Number of Movies'].max()
ator_mais_filmes = df.loc[df['Number of Movies'] == maior_num_filmes, 'Actor'].values[0]

# Gravar o resultado no arquivo "etapa-1"
with open('etapa-1.txt', 'w') as arquivo_saida:
    arquivo_saida.write(f"O ator/atriz com maior número de filmes é {ator_mais_filmes}, com um total de {maior_num_filmes} filmes.")

# Tarefa 2: Apresentar a média da coluna contendo o número de filmes
media_filmes = df['Number of Movies'].mean()

# Gravar o resultado no arquivo "etapa-2"
with open('etapa-2.txt', 'w') as arquivo_saida:
    arquivo_saida.write(f"A média de filmes é {media_filmes:.2f}")

# Tarefa 3: Apresentar o nome do ator/atriz com a maior média por filme
df['Average per Movie'] = df['Total Gross'] / df['Number of Movies']
ator_maior_media = df.loc[df['Average per Movie'].idxmax(), 'Actor']

# Gravar o resultado no arquivo "etapa-3"
with open('etapa-3.txt', 'w') as arquivo_saida:
    arquivo_saida.write(f"O ator/atriz com a maior média por filme é {ator_maior_media}")

# Tarefa 4: Apresentar o(s) filme(s) mais frequente(s) e sua respectiva frequência
frequencia_filmes = df['#1 Movie'].value_counts()
filme_mais_frequente = frequencia_filmes.idxmax()
frequencia_mais_frequente = frequencia_filmes.max()

# Gravar o resultado no arquivo "etapa-4"
with open('etapa-4.txt', 'w') as arquivo_saida:
    arquivo_saida.write(f"O(s) filme(s) mais frequente(s) é(são) '{filme_mais_frequente}', com uma frequência de {frequencia_mais_frequente}")
