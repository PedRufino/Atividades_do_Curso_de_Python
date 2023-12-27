# count é um iterador sem fim

from itertools import count

c1 = count()
r1 = range(10)

for i in c1:
    if i > 100:
        break
    print(i)