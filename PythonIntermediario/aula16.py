# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


certa = 0
errado = 0
count = 1
for item in perguntas:
    print(f'Pergunta {count}: {item["Pergunta"]}\n')
    for opcao in item['Opções']:
        print(f'é igual a {opcao}')
    resp = input('\nResposta: ')
    if resp != item['Resposta']:
        errado += 1
        print('Resposta Errada\n')
    else:
        certa += 1
        print('Acertouuu!!\n\n')
        continue
print(f'Acertos: {certa}\nErros: {errado}')
