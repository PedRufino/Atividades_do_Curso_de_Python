"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

import re
import sys
import random

# GERADOR DE CPF (NOVE PRIMEIROS NUMEROS)
# ================================================= #

cpf = ''
for i in range(9):
    cpf += str(random.randint(0,9))

# ================================================= #


# AULA63 (DADOS SEQUENCIAIS)
# ================================================= #
# cpf = '746.824.890-70'
# cpf = re.sub(r'[^0-9]','',cpf)

# sequencial = cpf == cpf[0] * len(cpf)
# if sequencial:
#     print('Você enviou dados sequenciais.')
#     sys.exit()

# ================================================= #


# AULA61
# ================================================= #
result = 0
for index, item in enumerate(cpf):
    result += (10 - index)*int(item)
result = (result*10) % 11

digito = result if result <= 9 else 0

# ================================================= #

# AULA62
# ================================================= #
# Parte 2: codigo de validação de cpf

cpf1 = cpf[:9] + str(result)
result_2 = 0
for index, item in enumerate(cpf1[:10]):
    result_2 += (11 - index)*int(item)
result_2 = (result_2*10) % 11


digito_2 = result_2 if result_2 <= 9 else 0

print(f'{cpf}{digito}{digito_2}')
# ================================================= #