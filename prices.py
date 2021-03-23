x, y, z = [0, 0, 0]
p = [80, 85, 95]
s = int(input("Введите сумму покупки "))
max = (s//min(p)) +1
if s > min(p) and s % 5 == 0:
    print("Б М А")
for x in range(max):
    for y in range(max):
        for z in range(max):
            if x*p[0] + y*p[1] + z*p[2] == s:
                print(x, y, z)
