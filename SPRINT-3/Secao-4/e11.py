#Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.

with open("arquivo_texto.txt", encoding='utf8') as f:
    for line in f:
        print(line, end='')