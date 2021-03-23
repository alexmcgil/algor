import random
n = int(input())
m = []
for i in range(n):
    m.append(random.randint(1, 20))
l, e, g = [], [], []

op = m[0]
for i in m:
    if i < op:
        l.append(i)
    elif i == op:
        e.append(i)
    else:
        g.append(i)
ans=l+e+g
print(m)
print(ans)