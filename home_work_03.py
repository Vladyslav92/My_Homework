#- Задачка про велосипедиста Васю.
v = int(input("Скорость: "))
t = int(input("Время: "))
b = 100
if v > 0:
	print("Вася движется в положительном направлении -", v * t, "км/ч")
	if v * t != b:
		print("Вася на отметке", v * t)
	elif v * t == b:
		print("Вася на отметке 100")
elif v < 0:
	print("Вася движется в отрицательном направлении -", v // t, "км/ч")
else:
	print("Вася стоит на месте.")

#- Задачка про выведение дробной части числа и выведении первой цифры после десятичной дроби.
x = float(input("Введите число"))
print(x - int(x))
print(int(x * 10) % 10)

#- Задачка про Сумму цифр трехзначного числа
a = int(input("Введите число: "))
a1 = a // 100
a2 = (a // 10) % 10
a3 = a % 10
print(a1 + a2 + a3)

#- Задачка про функцию sign(x)
b = int(input("Введите число: "))
if b > 0:
	print(1)
elif b < 0:
	print(-1)
else:
	print(0)

#-Задачка про высокосный год
year = int(input("Введите год: "))
if year % 4 !=0:
	print("NO")
elif year % 100 == 0:
	if year % 400 == 0:
		print("YES")
	else:
		print("NO")
else:
	print("YES")

#- Задачка про ход коня
x1 = int(input("Укажите координаты: "))
y1 = int(input("Укажите координаты: "))
x2 = int(input("Укажите координаты: "))
y2 = int(input("Укажите координаты: "))
if (x1 - 1 == x2 or x1 + 1 == x2) and (y1 - 2 == y2 or y1 + 1 == y2):
	print("YES")
elif (x1 - 2 == x2 or x1 + 2 == x2) and (y1 - 1 == y2 or y1 + 1 == y2):
	print("YES")
else:
	print("NO")
