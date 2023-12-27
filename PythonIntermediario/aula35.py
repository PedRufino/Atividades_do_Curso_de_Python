# try, except, else e finally

a = 18
b = 0

try:
    print(a[0])
    c = a / b
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('MSG:', error.__class__.__name__)
except Exception:
    print('Error Desconhecido')
else:
    print('Não deu erro')
finally:
    print('Final')

print('CONTINUAR')