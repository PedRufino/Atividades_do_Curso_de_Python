# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

# (pt2): Decoradoras são "Sysntax Sugar" (Açucar Sintático)


def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)

        result = func(*args, **kwargs)
        return result

    return interna

@criar_funcao
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError("Param deve ser uma string")


invert = inverte_string('123')
print(invert)
