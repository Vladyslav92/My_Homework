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

#2) -.

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
