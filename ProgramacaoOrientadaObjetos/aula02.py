# Métodos em instância de classes Python
# Entendendo self em classes Python

# self.nome = 'Fusca' # Hard Coded: Algo q foi escrito direto no código

# Classe - Molde (Geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar varias instâncias.
# Na classe o self é a própria instância.

class Carro:
    def __init__(self, nome):
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro('Celta')
print(celta.nome)
celta.acelerar()