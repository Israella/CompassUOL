#Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, Truese a lâmpada estiver ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos:
#liga(): muda o estado da lâmpada para ligada
#desliga(): muda o estado da lâmpada para desligada
#esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário

class Lampada:
    def __init__(self, ligada):
        self.ligada = ligada
    
    def liga(self):
        self.ligada = True
    
    def desliga(self):
        self.ligada = False
    
    def esta_ligada(self):
        return self.ligada
lampada = Lampada(True)
print("A lâmpada está ligada?", lampada.esta_ligada())  # Saída: A lâmpada está ligada? True

lampada.desliga()
print("A lâmpada ainda está ligada?", lampada.esta_ligada())  # Saída: A lâmpada ainda está ligada? False