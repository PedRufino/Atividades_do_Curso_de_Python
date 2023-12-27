# Variáveis livres + nonlocal (locals, globals)
# print(globals())
# def fora(x):
#     a=x #Variáveis Local
    
#     def dentro():
#         print(locals())
#         print(dentro.__code__.co_freevars)
#         return a
#     return dentro

# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())

def concatenar(string_ini):
    valor_final = string_ini
    
    def interna(valor_concat=''):
        nonlocal valor_final
        valor_final += valor_concat
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))