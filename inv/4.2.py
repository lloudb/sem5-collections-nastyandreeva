4.2. Создание программы по распределению списка с случайными значениями на два списка по определенному критерию положительные/отрицательные.

import random
array = []

for i in range(10):
    array.append(int(random.random() * 10) - 5)
 
positive_num = []
negative_num = []

for i in array:
    if i < 0:
        negative_num.append(i)
    elif i > 0:
        positive_num.append(i)
        
print(positive_num)
print(negative_num)
