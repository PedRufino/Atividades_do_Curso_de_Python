# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    total = 1
    for num in args:
        total *= num
    return total

result = multiplicar(1,3,4,5,10)
print(result)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    
    if multiplo_de_dois:
        return f'{numero} é Par'
    return f'{numero} é Impar'

result = par_impar(1)
print(result)
