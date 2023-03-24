# Abrindo o arquivo actors.cvs e lendo as linhas:

with open('actors.csv', 'r') as f:
    lines = f.readlines()[1:]

# Criando as listas para armazenar os dados:

actors = []
total_gross = []
number_movies = []
avg_movie = []
top_movie = []
gross = []

# Corrigindo a linha 4 que contem erro na virgula:

lines[4] = '"Robert Downey Jr.",3947.30 ,53,74.50 ,The Avengers,623.40'

# Armazenando os dados de acordo com as listas:

for line in lines:

    actor = line.split(',')
    tgross = line.split(',')
    nmovies = line.split(',')
    avg = line.split(',')
    tmovie = line.split(',')
    g = line.split(',')

    actors.append(actor[0])
    total_gross.append(tgross[1])
    number_movies.append(nmovies[2])
    avg_movie.append(avg[3])
    top_movie.append(tmovie[4])
    gross.append(g[5])

# Convertendo os valores de string para float:

number_movies = [int(n) for n in number_movies]
total_gross = [float(g) for g in total_gross]
avg_movie = [float(a) for a in avg_movie]
gross = [float(g) for g in gross]

# 1- Apresente o ator/atriz com maior número de filmes e a respectiva quantidade.

max_number_movies = max(number_movies)
index_max_number_movies = number_movies.index(max_number_movies)
actors_more_movies = actors[index_max_number_movies]

# Passando o resultado para etapa-1.txt:

with open('etapa-1.txt', 'w') as f:
    f.write(f"{actors_more_movies}, Participou de {max_number_movies} filmes.")

# 2- Apresente a  média de faturamento bruto por ator.

avg_per_actors = {}
for i in range(len(actors)):
    if actors[i] in avg_per_actors:
        avg_per_actors[actors[i]] += total_gross[i]/number_movies[i]
    else:
        avg_per_actors[actors[i]] = total_gross[i]/number_movies[i]

# Arredondando o valor da média para 2 casas decimais:

for actor, avg in avg_per_actors.items():
    avg_per_actors[actor] = round(avg, 2)

# Passando o resultado para etapa-2.txt:

with open('etapa-2.txt', 'w') as f:
    for actor, avg in avg_per_actors.items():
        f.write(f"{actor}, {avg}.\n")

# 3- Apresente o ator/atriz com a maior média de faturamento por filme.

max_avg_movie = max(avg_movie)
idx_max_avg_movie = avg_movie.index(max_avg_movie)
actor_max_avg_gross = actors[idx_max_avg_movie]

# Passando o resultado para etapa-3.txt:

with open('etapa-3.txt', 'w') as f:
    f.write(f"{actor_max_avg_gross}.Com uma media de faturamento de {max_avg_movie}.")

# 4- O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

freq_movie = {}
for m in top_movie:
    if m in freq_movie:
        freq_movie[m] += 1
    else:
        freq_movie[m] = 1

max_freq = max(freq_movie.values())
most_freq_movie = [k for k, v in freq_movie.items() if v == max_freq]

# Passando o resultado para etapa-4.txt:

with open('etapa-4.txt', 'w') as f:
    if len(most_freq_movie) == 1:
        f.write(f"{most_freq_movie[0]}'. Aparecendo {max_freq} vezes.")
    else:
        movies_str = ', '.join(most_freq_movie)
        f.write(f"{movies_str}'. Aparecendo {max_freq} vezes.")

# 5- A lista dos atores ordenada pelo faturamento bruto total, em ordem decrescente.

total_gross_a = {}
for i in range(len(actors)):
    if actors[i] in total_gross_a:
        total_gross_a[actors[i]] += total_gross[i]
    else:
        total_gross_a[actors[i]] = total_gross[i]

sorted_actors = [(k, v) for k, v in sorted(total_gross_a.items(), key=lambda item: item[1], reverse=True)]

# Passando o resultado para etapa-5.txt:

with open('etapa-5.txt', 'w') as f:
    for actor, gross in sorted_actors:
        f.write(actor +","+ str(gross) +"\n")