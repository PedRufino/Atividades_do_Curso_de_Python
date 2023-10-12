nome = 'Pedro Neto'
altura = 1.70
peso = 80
imc = peso / (altura ** 2)

# f-strings
print(f'''
{nome} tem {altura:.2f} de altura,
pesa {peso:.1f} quilos e seu IMC é
{imc:.2f}
''')

# Pedro Neto tem 1.70 de altura,
# pesa 95 quilos e seu IMC é
# 27.68166089965398
