
# Соседи слева и справа
lst = [int(i) for i in input("Введите числа: ").split()]
counter = 0
for i in range(1, len(lst) - 1):
    if lst[i - 1] < lst[i] > lst[i + 1]:
        counter += 1
print("Кол-во элементов, которые больше двух своих соседей -", counter)

# Петя перешел в другую Школу, СТРОЙ
a = input("Рост людей - ").split()
x = int(input("Рост Пети - "))
x_index = 0
a.sort(reverse = True)
for i in range(0, len(a)):
    n = int(a[i])
    if n >= x:
        x_index = i + 1
print(a)
print("Позиция -", x_index + 1)

# ИЛИ

from random import randint
x = int(input("Кол-во школьников: "))
a = [randint(100, 200) for a in range(x)]
a.sort(reverse=True)
print(a)
x = int(input("Рост Пети: "))
x_index = 0
for i in range(0, len(a)):
    n = int(a[i])
    if n >= x:
        x_index = i + 1
print(x_index + 1)

# Задача Удалить Элемент
a = [int(s) for s in input("Введите числа - ").split()]
k = int(input("Введите число - "))
for i in range(k + 1, len(a)):
    a[i - 1] = a[i]
a.pop()
print(' '.join([str(i) for i in a]))
