def conta_vogais(texto:str)-> int:
    vogais = 'aeiouAEIOU'
    return len(list(filter(lambda x: x in vogais, texto)))