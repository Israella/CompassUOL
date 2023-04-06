import csv
with open('estudantes.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    notas = []
    for row in reader:
        nome = row[0]
        notas_aluno = [float(nota) for nota in row[1:]]
        notas.append((nome, notas_aluno))

notas = sorted(notas, key=lambda x: x[0])

for aluno in notas:
    nome = aluno[0]
    notas_aluno = aluno[1]
    notas_ordenadas = sorted(notas_aluno, reverse=True)
    maiores_notas = notas_ordenadas[:3]
    media = round(sum(maiores_notas) / 3, 2)
    notas_formatadas = list(map(lambda n: int(n), maiores_notas))
    saida = f"Nome: {nome} Notas: {notas_formatadas} Média: {media}"
    print(saida)
