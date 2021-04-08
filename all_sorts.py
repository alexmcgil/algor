def printhash():
    print("############################")


def qsort(items):
    lower, equal, greater = [], [], []
    if len(items) > 1:
        # Определяем курсор на первом элементе массива
        cursor = items[0]
        for i in items:
            # Помещаем в массив lower элементы меньшие чем курсор
            if i < cursor:
                lower.append(i)
                # Помещаем в массив equal элементы равные курсору
            elif i == cursor:
                equal.append(i)
            else:
                # Помещаем в массив greater элементы большие чем курсор
                greater.append(i)
        return qsort(lower) + equal + qsort(greater)  # Возвращаем массивы отсортировываться до конца через рекурсию
    else:
        return items  # Если массивы отсортированы, заканчиваем


def bubble(items):
    for k in items:
        for i in range(n - 1):
            # Если нашёлся меньший элемент, меняем их местами
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
    return items


def insert(items):
    for i in range(n):
        cursor = items[i]
        pos = i
        while pos > 0 and items[pos - 1] > cursor:
            items[pos] = items[pos - 1]
            pos = pos - 1
        items[pos] = cursor

    return items


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # Создадим переменные 
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


def selection_sort(items):
    for i in range(0, len(items) - 1):
        smallest = i
        for j in range(i + 1, len(items)):
            if items[j] < items[smallest]:
                smallest = j
        items[i], items[smallest] = items[smallest], items[i]
    print(items)
