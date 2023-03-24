#Dada a seguinte lista:
#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#Faça um programa que gere uma nova lista contendo apenas números ímpares.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Utilizando list comprehension para gerar nova lista contendo apenas números ímpares
impares = [x for x in a if x % 2 != 0]

# Imprime a nova lista na saída padrão
print(impares)