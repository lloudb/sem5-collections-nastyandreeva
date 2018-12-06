4.1 Создание программы по заполнению массивов случайными значениями. Сортировка значений в списке методом вставки, плавной сортировки, с помощью встроенных функций языка.

# Подключаем библиотеку numpy для создания и выполнений операций с массивами 
import numpy as np
import numpy.random 

# Создание массива со случайными 10 целыми числами от 0 до 15
array = np.random.randint(0, 15, 10)

# Cортировка по возрастанию/убыванию
sort_array = sorted(array)
reverse_array = sorted(array, reverse = True)
# Случайная выборка из массива, с помощью функции choice
rand_array = np.random.choice(array, 20, replace = True)
# Функция permutation позволяет перемешать и возвратить полученный массив
per_array = np.random.permutation(array)

print("Массив со случайными целыми числами")
print(array)
print("")
print("Сортировка  с помощью встроенных функций: ")
print("")
print("Сортировка массива по возрастанию")
print(sort_array)

print("Сортировка массива по убыванию")
print(reverse_array)
 
print("Перемешанный массив")
print(per_array)

print("Случайна выборка из массива")
print(rand_array)

# Сортировка простыми вставками
def just_sort(lst = np.random.randint(0, 15, 10)):
    for i in range(len(lst) - 1):
        j = i - 1 
        key = lst[i]
        while lst[j] > key and j >= 0:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst
print("")
print("Сортировка простыми вставками")
print(just_sort())


# Плавная сортировка
def Smooth_Sort(lst):
    def downHeap(lst, k, n):
        new_elem = lst[k]
        while 2*k+1 < n:
            child = 2*k+1
            if child+1 < n and lst[child] < lst[child+1]:
                child += 1
            if new_elem >= lst[child]:
                break
            lst[k] = lst[child]
            k = child
        lst[k] = new_elem
    size = len(lst)
    for i in range(size//2-1,-1,-1):
        downHeap(lst, i, size)
    for i in range(size-1,0,-1):
        temp = lst[i]
        lst[i] = lst[0]
        lst[0] = temp
        downHeap(lst, 0, i)
    return lst
print("")
print("Плавная сортировка")
print(Smooth_Sort(array))
