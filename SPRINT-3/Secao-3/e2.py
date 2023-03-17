numeros = []
for i in range(3):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))

# Verifica se cada número é par ou ímpar
for num in numeros:
    if num % 2 == 0:
        print(f"Par: {num}")
    else:
        print(f"Ímpar: {num}")