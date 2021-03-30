import random
n = int(input("Введите сложность массива  "))
m = []
for r in range(n):
    m.append(1)

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
    print(m)

def bubble(m):
    for k in m:
        for i in range(n-1):
            if m[i] > m[i+1]:
                m[i], m[i+1] = m[i+1], m[i]
    print(m)

def insert(m):

    for i in range(n):
        cursor = m[i]
        pos = i
        while pos > 0 and m[pos - 1] > cursor:
            m[pos] = m[pos - 1]
            pos = pos - 1
        m[pos] = cursor

    return m
    print(m)

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # Длина списков часто используется, поэтому создадим переменные для удобства
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его
            # в отсортированный массив
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его
            # в отсортированный массив
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Если достигнут конец левого списка, элементы правого списка
        # добавляем в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Если достигнут конец правого списка, элементы левого списка
        # добавляем в отсортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):
    # Возвращаем список, если он состоит из одного элемента
    if len(nums) <= 1:
        return nums

    # Для того чтобы найти середину списка, используем деление без остатка
    # Индексы должны быть integer
    mid = len(nums) // 2

    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)



def selection_sort(m):
    for i in range(0, len(m) - 1):
        smallest = i
        for j in range(i + 1, len(m)):
            if m[j] < m[smallest]:
                smallest = j
        m[i], m[smallest] = m[smallest], m[i]
    print(m)

sel = int(input("Веедите вариант сортировки: 1 - bubble, 2 - quicksort, 3 - insert, 4 - merge, 5 - selection:\n"))

#def switch_func(sel):
 #   switcher = {
  #      1: bubble(m)
    #    2: qsort(m),
   #     3: insert(m),
   #     4: smerge(m),
   #     5: selection_sort(m),
  #  }
  #  print(switcher.get(sel))

if sel == 1:
    print(bubble(m))
elif sel == 2:
    print(qsort(m))
elif sel == 3:
    print(insert(m))
elif sel == 4:
    print(merge_sort(m))
elif sel == 5:
    print(selection_sort(m))
else:
    print("Ошибка ввода")