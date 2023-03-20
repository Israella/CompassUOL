#Escreva um código Python para verificar se três números digitados na entrada padrão são pares ou ímpares. Para cada número, imprima como saída Par: ou Ímpar: e o número correspondente (um linha para cada número lido).
#Importante: Aplique a função range() em seu código.



numeros = []
for i in range(3):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))

# Verifica se cada número é par ou ímpar
for num in numeros:
    if num % 2 == 0:
        print(f"Par: {num}")
    else:
        print(f"Ímpar: {num}")