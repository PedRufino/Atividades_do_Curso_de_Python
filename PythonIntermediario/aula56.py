import json

# pessoa = {
#     'nome':'Pedro',
#     'sobrenome': 'Rufino',
#     'endereco': [
#         {'rua': 'R1', 'numero':32},
#         {'rua': 'R2', 'numero':55},
#     ],
#     'altura': 1.7,
#     'numeros_preferidos':(27,38,19,22,10),
#     'dev': True,
#     'nada': None
# }

# with open('aula56.json', 'w') as arquivo:
#     json.dump(
#         pessoa, 
#         arquivo, 
#         ensure_ascii=False, 
#         indent=4
#     )

with open('aula56.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)