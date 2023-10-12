a = 'AAAA'
b = 'BBBB'
c = 1.1

# Forma 2
string = 'a = {nome1} b = {nome2} c = {nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c) #nome3 = Parameto

# Forma 1
# formato = 'a = {} b = {}'.format(a, b, c)

print(formato)