# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


# def soma():
#     def duplicar(num):
#         return num * 2
#     def triplicar(num):
#         return num * 3
#     def quadruplicar(num):
#         return num * 4
#     return duplicar, triplicar, quadruplicar

# def executar(num, *args):
#     total = []
#     for function in args:
#         total.append(function(num))
#     return total

# v = soma()
# print(executar(2, *v))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))