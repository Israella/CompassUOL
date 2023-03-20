#Considere as duas listas abaixo:
#a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#Escreva um programa para avaliar o que ambas as listas têm em comum (sem repetições), imprimindo a lista de valores da interseção na saída padrão.

a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# converte as listas em conjuntos (sets)
set_a = set(a)
set_b = set(b)

# interseção dos conjuntos
intersecao = set_a.intersection(set_b)

# converte o resultado de volta em uma lista
resultado = list(intersecao)

# imprime o resultado na saída padrão
print(resultado)
