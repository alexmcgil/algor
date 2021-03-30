import random
n = int(input())
m = []
for r in range(n):
    m.append(random.randint(1, 20))

def selection_sort(m):
    for i in range(0, len(m) - 1):
        smallest = i
        for j in range(i + 1, len(m)):
            if m[j] < m[smallest]:
                smallest = j
        m[i], m[smallest] = m[smallest], m[i]

print(selection_sort(m))