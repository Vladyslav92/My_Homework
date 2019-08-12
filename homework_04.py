#1) Задача про спортсмена
# Общий пробег.
distance_per_day = int(input("Сколько км спортсмен пробежал за день? - "))
distance_end = int(input("Какое расстояние ему нужно пробежать? - "))
day = 0
need = distance_end
while need > 0:
    need -= distance_per_day
    distance_per_day *= 1.1
    day += 1
print("Пробежал за {} дней".format(day))

# Пробег в определенный день.
x = int(input("Сколько км спортсмен пробежал в первый день? - "))
y = int(input("Какое расстояние ему нужно пробежать? - "))
day = 1
while x < y:
    x *= 1.1
    day += 1
print("На {} день".format(day))

#2)
enter = 1
counter = 0
summ = 0
composition = 1
mmax = 0
index_of_max = 0
second_largest = 0
greatest_num = 0
even_counter = 0
odd_counter = 0
while enter != 0:
    enter = int(input('Введите числа: '))
    if enter < 0:
        continue
    elif enter == 0:
        break
    counter += 1
    summ += enter
    composition *= enter
    if enter > mmax:
        second_largest = mmax
        greatest_num = 1
        mmax = enter
        index_of_max = counter
    elif enter == mmax:
        greatest_num += 1
    if enter/2 == enter//2:
        even_counter += 1
    else:
        odd_counter += 1
print()
print('Кол-во чисел -', counter)
print('Сумма чисел -', summ)
print('Произведение чисел -', composition)
print('Среднее арифметическое -', summ/counter)
print('Наибольшее число -', mmax)
print('Номер наибольшего числа -', index_of_max)
print('Кол-во четных -', even_counter)
print('Кол-во нечетных -', odd_counter)
print('Второе наибольшее число -', second_largest)
print('Кол-во наибольших чисел -', greatest_num)

#3) Задачка про выведения чисел по возрастанию от A до B если A < B или по убыванию в противном случае.
A = int(input("Введите первое число: "))
B = int(onput("Введите второе число: "))
if A < B:
	for i in range(A, B + 1):
		print(i)
else:
	for i in range(A, B - 1, -1):
		print(i)

#4) Задачка про выведению нечетных чисел в порядке убывания от А до Б
a = int(input("Введите число: "))
b = int(input("Введите число: "))
for i in range(a - (a + 1) % 2, b - b % 2, -2):
	print(i, end = '\n')

#5) Задачка про лесенку из чисел.
n = int(input("Число: "))
for i in range(1, n + 1):
	for j in range(1, i + 1):
		print(j, sep = '', end + '')
	print()
