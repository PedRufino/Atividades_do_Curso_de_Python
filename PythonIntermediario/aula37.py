# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import aula37_m
from aula37_m import soma, var_modulo

# print('Este modulo se chama', __name__)
print(var_modulo)
print(soma(1, 2))
print(aula37_m.soma(1, 2))