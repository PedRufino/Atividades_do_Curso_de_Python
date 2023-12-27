# raise - lançando exceções (erros)

# print(123)
# raise ValueError('Deu erro')
# print(456)

# def divide(n, d):
#     try:
#         return n / d 
#     # Redundancia
#     except ZeroDivisionError:
#         raise

def not_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está dividindo por Zero')
    return True

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'{n} deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado'
        )

def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    not_zero(d)
    return n / d

print(divide(8, '0'))