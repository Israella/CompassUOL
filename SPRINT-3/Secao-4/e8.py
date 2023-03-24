#Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou não um palíndromo.
#Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente.

palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

# Itera sobre cada palavra da lista
for palavra in palavras:
    # Inverte a palavra utilizando slicing
    palavra_invertida = palavra[::-1]
    # Verifica se a palavra original é igual à palavra invertida
    if palavra == palavra_invertida:
        print("A palavra:", palavra, "é um palíndromo")
    else:
        print("A palavra:", palavra, "não é um palíndromo")
