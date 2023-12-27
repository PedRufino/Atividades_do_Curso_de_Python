# List Comprehension em Python
# List Comprehension é uma forma rápida para criar listas
# a partir de iteráveis

import pprint

# print(list(range(10)))

def p(v):
    return pprint.pprint(v, sort_dicts=False)

lista=[]

for numero in range(10):
    lista.append(numero)
# print(lista)

lista=[
    numero * 2
    for numero in range(10)
]
# print(list(range(10)))
# print(lista)

# Mapeamneto de dados em list comprehension
produtos = [
    {'nome':'p1', 'preco': 20},
    {'nome':'p2', 'preco': 10},
    {'nome':'p3', 'preco': 30},
]

novos_produto = [
    {**produto, 'preco': produto['preco']*1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]

p(novos_produto)

# print(novos_produto)
# print(*novos_produto, sep="\n")

# p(novos_produto)

# o que vem na direita do for é FILTRO
# já na esquerda é MAPEAMENTO

lista = [n for n in range(10) if n < 5]
p(lista)