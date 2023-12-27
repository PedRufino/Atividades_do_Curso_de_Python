# Dictionary Comprehension e Set Comprehension

produto = {
    "nome": "Caneta Azul",
    "preco": 2.5,
    "categoria": "Escritório",
}

# for chave, valor in produto.items():
#     print(chave, valor)

dc = {
    chave: valor.upper() if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != "categoria"
}

lista = [
    ("a", "valor a"),
    ("b", "valor b"),
    ("c", "valor c"),
]

dc = {chave: valor for chave, valor in lista}

# print(dc)
# print(dict(lista))

s1 = {2**i for i in range(10)}
print(s1)
print(set(range(10)))
