# Generator expression, Iterables e Iterators em Python
import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__

lista = [n for n in range(1000000)]
generetor = (n for n in range(1000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generetor))

for n in generetor:
    print(n)