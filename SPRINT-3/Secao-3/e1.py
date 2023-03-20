import datetime

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
ano_atual = datetime.datetime.now().year

ano_100 = ano_atual + (100 - idade)


print(ano_100)