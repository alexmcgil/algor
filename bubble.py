#import random
#n = int(input())
m = [5, 1, 4, 2, 8]
#for i in range(n):
#    m.append(random.randint(1,20))
for k in m:
    for i in range(4):
        if m[i] > m[i+1]:
            m[i], m[i+1] = m[i+1], m[i]
print(m)