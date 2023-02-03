from isOdd import isOdd
import random

list1 = []
n = int(input('Введите количество элементов: '))
for _ in range(n):
    list1.append(random.randint(0, 5))
print('исходный список: ', list1)

list2 = []
for i in range(0, (len(list1))):
    if isOdd(list1[i]):
        list2.append(list1[i]**2)
print(f'список квадратов нечетных элементов: {list2}')
