#Crie uma classe Avião que possua os atributos modelo, velocidade_maxima, cor e capacidade.
#Defina o atributo cor de sua classe , de maneira que todas as instâncias de sua classe avião sejam da cor “azul”.
#Após isso, a partir de entradas abaixo, instancie e armazene em uma lista 3 objetos da classe Avião.
#Ao final, itere pela lista imprimindo cada um dos objetos no seguinte formato:
#“O avião de modelo “x” possui uma velocidade máxima de “y”, capacidade para “z” passageiros e é da cor “w”.
#Sendo x, y, z e w cada um dos atributos da classe “Avião”.

class Aviao:
    cor = "Azul"
    
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        
avioes = []
avioes.append(Aviao("BOIENG456", "1500 km/h", 400))
avioes.append(Aviao("Embraer Praetor 600", "863 km/h", 14))
avioes.append(Aviao("Antonov An-2", "258 km/h", 12))

for aviao in avioes:
    print(f"O avião de modelo {aviao.modelo} possui uma velocidade máxima de {aviao.velocidade_maxima}, capacidade para {aviao.capacidade} passageiros e é da cor {aviao.cor}.")