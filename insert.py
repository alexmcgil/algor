import random
n = int(input())
m = []
for r in range(n):
    m.append(random.randint(1, 20))

def insert(m):

    for i in range(len(m)):
        cursor = m[i]
        pos = i
        while pos > 0 and m[pos - 1] > cursor:
            m[pos] = m[pos - 1]
            pos = pos - 1
        m[pos] = cursor

    return m