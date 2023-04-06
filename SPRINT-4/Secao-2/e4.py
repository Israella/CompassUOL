def calcular_valor_maximo(operadores, operandos) -> float:
    operacoes = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '%': lambda x, y: x % y
    }
    resultados = list(map(lambda x: operacoes[x[0]](x[1][0], x[1][1]), zip(operadores, operandos)))
    return max(resultados)