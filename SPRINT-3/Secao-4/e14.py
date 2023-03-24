#Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido


def imprimir_parametros(*args, **kwargs):
    # Imprimindo os parâmetros não nomeados
    for parametro in args:
        print(parametro)

    # Imprimindo os parâmetros nomeados
    for chave, valor in kwargs.items():
        print(chave, "=", valor)


# Chamando a função com os parâmetros fornecidos
imprimir_parametros(1, 3, 4, 'hello','alguma coisa', 20)
