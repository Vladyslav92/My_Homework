#9. Задание.
n = int(input("Кол-во Школьников: "))
k = int(input("Кол-во Яблок: "))
sum = k / n
sum2 = k % n
print("Каждому школьнику достанется", sum, "яблок")
print("В корзинке", sum2, "яблок")

#ИЛИ

n = int(input("Кол-во Школьников: "))
k = int(input("Кол-во Яблок: "))
print("Каждому школьнику достанется {} яблок\nВ корзине {} яблок".format(k / n, k % n))

#10. Задание.
n = int(input("Введите число: "))
hours = n // 60 % 24
minutes = n % 60
print("Сейчас {} часов и {} минут".format(hours, minutes)

#11. Задание.
hi = input("Hello! What\'s your name? ")
name = "Hello " + hi + "!"
print(name)

#12. Задание.
num = int(input('Enter the number: '))
print("The next number for the number {} is: {}".format(num, num + 1)
      + "\nThe pervious number for the number {} is: {}".format(num, num - 1))

#13. Задание.
class1 = int(input("Кол-во Учеников в первом классе: "))
class2 = int(input("Кол-во Учеников во втором классе: "))
class3 = int(input("Кол-во Учеников в третем классе: "))
sum = round((class1 + class2 + class3)/2)
print("Количество парт: ", sum)
