# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

n = int(input('Введите n: '))
list = list()

while n > 0:
    list.append(n % 2)
    n //= 2

dv = ''
for i in range(len(list)-1, -1, -1):
    dv += str(list[i])

print(dv)