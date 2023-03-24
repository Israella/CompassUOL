#Implemente duas classes Pato e Pardal que herdem de uma classe Passaro a habilidade de voar e emitir som, porém, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console.

class Passaro:
    def voar(self):
        print("Voando...")
    
    def emitir_som(self):
        pass

class Pato(Passaro):
    def emitir_som(self):
        print("Pato emitindo som...")
        print("Quack Quack")

class Pardal(Passaro):
    def emitir_som(self):
        print("Pardal emitindo som...")
        print("Piu Piu")

# Testando as classes
pato = Pato()
print("Pato")
pato.voar()
pato.emitir_som()

pardal = Pardal()
print("Pardal")
pardal.voar()
pardal.emitir_som()