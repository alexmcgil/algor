import time
import numpy as np
from all_sorts import *
n = int(input("Введите сложность массива: "))
items = np.random.randint(0, n, n)
printhash()
print(items)
printhash()
print("Веедите вариант сортировки:\n1 - bubble\n2 - quicksort\n3 - insert\n4 - merge\n5 - selection:")
sel = int(input())
printhash()


def toFixed(numObj, digits=10):
    return f"{numObj:.{digits}f}"

if sel == 1:
    starttime = time.time()
    print(bubble(items))
    printhash()
    print(toFixed((time.time() - starttime)), "seconds")
elif sel == 2:
    starttime = time.time()
    print(qsort(items))
    printhash()
    print(toFixed((time.time() - starttime)), "seconds")
elif sel == 3:
    starttime = time.time()
    print(insert(items))
    printhash()
    print(toFixed((time.time() - starttime)), "seconds")
elif sel == 4:
    starttime = time.time()
    print(merge_sort(items))
    printhash()
    print(toFixed((time.time() - starttime)), "seconds")
elif sel == 5:
    starttime = time.time()
    print(selection_sort(items))
    printhash()
    print(toFixed((time.time() - starttime)), "seconds")
else:
    print("Ошибка ввода")
printhash()

