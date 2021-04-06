s = 0
for i in range(1, 2000, 2):
    s += i
print(s)
s2 = 0
j = 1
while j <= 1999:
    s2 += j
    j += 2
print(s2)
sum = 0

for i in range(0, 2000):
    if i % 2 != 0:
        sum += i

print(sum)