4.2. Создание программы по распределению списка с случайными значениями на два списка по определенному критерию (четность/нечетность, положительные/отрицательные числа).

#Положительные/отрицательные

import random
array = []

for i in range(10):
    array.append(int(random.random() * 12) - 7)
 
positive_num = []
negative_num = []

for i in array:
    if i < 0:
        negative_num.append(i)
    elif i > 0:
        positive_num.append(i)
print("Списики со случайными значениями(положительные/отрицательные)")      
print(positive_num)
print(negative_num)

# Чётные/нечётные
array2 = []
for i in range(10):
    array2.append(int(random.random() * 15))
    
array2.sort()

num_even = list(filter(lambda x: not x%2, array2))
num_odd = list(filter(lambda x: x%2, array2))

print("Списики со случайными значениями(чётные/нечётные)")
print(num_even)
print(num_odd)
