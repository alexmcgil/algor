import random
n = int(input())
m = []
for i in range(n):
    m.append(random.randint(1, 20))
def qsort(m):
    l, e, g = [], [], []
    if len(m) > 1:
        op = m[0]
        for i in m:
            if i < op:
                l.append(i)
            elif i == op:
                e.append(i)
            else:
                g.append(i)
        return qsort(l)+e+qsort(g)
    else:
        return m
print(qsort(m))