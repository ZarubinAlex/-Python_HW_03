# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.ДОП
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

n = int(input('Введите n: '))
list = []
a0 = 0
a1 = 1

for i in range(n+1):
    list.append(a0)
    x = a0 + a1
    a0 = a1
    a1 = x

list2 = [list[i] * (-1)** (i+1) for i in range(len(list))]

print(list2[:0:-1] + list)