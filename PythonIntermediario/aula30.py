# dir, hasattr, getattr em Python
string = 'Pedro'
metodo = 'upper'

print(string)

if hasattr(string, 'upper'):
    print('Existe upper')
    print(getattr(string, metodo)())
    print(string)
else:
    print('Não existe o método', metodo)