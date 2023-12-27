# isinstace - para saber se o objeto é de determinado tipo

lista = ["a", 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {"nome": "Pedro"}]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print(item, isinstance(item, set))
        print('SET')
        
    elif isinstance(item, str):
        print('STR')
        print(item.upper(), isinstance(item, set))
    
    elif isinstance(item, (int,float)):
        print('NUM')
        print(item, item * 2)
    
    else:
        print('OUTRO')
        print(item)