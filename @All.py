import random
n = int(input("Введите сложность массива  "))
m = []
for r in range(n):
    m.append(random.randint(1, n))

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

def bubble(m):
    for r in range(n):
        m.append(random.randint(1, 20))
    for k in m:
        for i in range(n-1):
            if m[i] > m[i+1]:
                m[i], m[i+1] = m[i+1], m[i]

def mergeSort(m):
    if len(m)>1:
        mid = len(m)//2
        lefthalf = m[:mid]
        righthalf = m[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                m[k]=lefthalf[i]
                i=i+1
            else:
                m[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            m[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            m[k]=righthalf[j]
            j=j+1
            k=k+1

def insert(m):

    for i in range(n):
        cursor = m[i]
        pos = i
        while pos > 0 and m[pos - 1] > cursor:
            m[pos] = m[pos - 1]
            pos = pos - 1
        m[pos] = cursor

    return m

def merge(left, right, merged):
    lc, rc = 0, 0
    while lc < len(left) and rc < len(right):

        if left[lc] <= right[rc]:
            merged[lc + rc] = left[lc]
            lc += 1
        else:
            merged[lc + rc] = right[rc]
            rc += 1

    for lc in range(lc, len(left)):
        merged[lc + rc] = left[lc]

    for rc in range(rc, len(right)):
        merged[lc + rc] = right[rc]

    return merged


def smerge(m):
    if len(m) <= 1:
        return m
    mid = len(m) // 2
    left, right = smerge(m[:mid]), smerge(m[mid:])

    return smerge(left, right, m.copy())


def selection_sort(m):
    for i in range(0, len(m) - 1):
        smallest = i
        for j in range(i + 1, len(m)):
            if m[j] < m[smallest]:
                smallest = j
        m[i], m[smallest] = m[smallest], m[i]

sel = int(input("Веедите вариант сортировки: 1 - bubble, 2 - quicksort, 3 - insert, 4 - merge, 5 - selection:\n"))

#def switch_func(sel):
 #   switcher = {
  #    2: qsort(m),
    #    3: insert(m),
     #   4: smerge(m),
      #  5: selection_sort(m),
    #}
    #print(switcher.get(sel))

