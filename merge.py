import random
n = int(input())
m = []
for r in range(n):
    m.append(random.randint(1, 20))


def smerge(m):
    if len(m) <= 1:
        return m
    mid = len(m) // 2
    left, right = smerge(m[:mid]), smerge(m[mid:])

    return smerge(left, right, m.copy())


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