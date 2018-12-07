4.3. Создание программы, позволяющей выполнять основные операции (объединение, пересечение, вычитание) над множествами (количество элементов в множестве и их элементы вводятся вручную).
def set_array(count: int):
    i = 1
    arrays = []
    while i <= count:
        a = input("Введите множество " + str(i) + ": ")
        a = a.split(",")
        for j in range(len(a)):
            a[j] = int(a[j])
        arrays.append(a)
        i += 1
    return arrays

def calc():
    count_arrays = int(input(' Введите количество множеств:\n'))
    choice = input(' Введите номер действия: \n 1.Объединение, 2.Пересечение, 3.Вычитание\n')

    if choice == '1':
        arrays = set_array(count_arrays)
        result = set(arrays[0])
        for i in range(1, len(arrays)):
            result |= set(arrays[i])
        print("Результат:", result)
    elif choice == '2':
        arrays = set_array(count_arrays)
        result = set(arrays[0])
        for i in range(1, len(arrays)):
            result &= set(arrays[i])
        print("Результат:", result)
    elif choice == '3':
        arrays = set_array(count_arrays)
        result = set(arrays[0])
        for i in range(1, len(arrays)):
            result -= set(arrays[i])
        print("Результат:", result)
    else:
        print('Некорректный ввод')

calc()
