
# Desenvolva um código Python que lê do teclado nome e a idade atual de uma pessoa. 
# Como saída, imprima o ano em que a pessoa completará 100 anos de idade.



import datetime

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
ano_atual = datetime.datetime.now().year

ano_100 = ano_atual + (100 - idade)


print(ano_100)