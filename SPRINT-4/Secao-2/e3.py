from functools import reduce

def calcula_saldo(lancamentos) -> float:
    valores = list(map(lambda x: -x[0] if x[1] == 'D' else x[0], lancamentos))
    return reduce(lambda acc, x: acc + x, valores)