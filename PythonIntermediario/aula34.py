# Yield from

def gen1():
    yield 1
    yield 2
    yield 3
    print('Acabou Gen1')

def gen3():
    yield 10
    yield 20
    yield 30
    print('Acabou Gen3')

def gen2(gen):
    yield from gen()
    yield 4
    yield 5
    yield 6
    print('Acabou Gen2')

g1 = gen2(gen1)
g2 = gen2(gen3)
for num in g1:
    print(num)
for num in g2:
    print(num)