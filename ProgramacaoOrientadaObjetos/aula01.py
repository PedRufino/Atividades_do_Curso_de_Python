# Introdução ao método __init__ (inicializador de atributos)
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Pedro', 'Neto')
# p1.nome='Pedro'
# p1.sobrenome='Rufino'

p2 = Pessoa('Julia', 'da Silva')
# p2.nome='Julia'
# p2.sobrenome='da Silva'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)