# 1. Питон установил на Linux через pip.

# 2. Скачал и установил бесплатную версию PyCharm.

# 3.
#a) - import this
#Выводит The Zen of Python, by Tim Peters и ниже пишет правила:
#- Beautiful is better than ugly.
#- Explicit is better than implicit.
#- Simple is better than complex.
#- Complex is better than complicated.
#- Flat is better than nested.
#- Sparse is better than dense.
#- Readability counts.
#- Special cases aren't special enough to break the rules.
#- Although practicality beats purity.
#- Errors should never pass silently.
#- Unless explicitly silenced.
#- In the face of ambiguity, refuse the temptation to guess.
#- There should be one-- and preferably only one --obvious way to do it.
#- Although that way may not be obvious at first unless you're Dutch.
#- Now is better than never.
#- Although never is often better than *right* now.
#- If the implementation is hard to explain, it's a bad idea.
#- If the implementation is easy to explain, it may be a good idea.
#- Namespaces are one honking great idea -- let's do more of those!
#b) - import antigravity
#Перенес меня на сайт с комиксом о Питоне https://xkcd.com/353/
#c) - imort __hello__
#Вывел в консоли Hello world!
#d) - from __future__ import braces
#Вывел ошибку SytaxError: not a chance
#В интернете пишут что это шутка)

#4.
print('******\t    **  \t    **\t      *****\n'
      '*    * \t   *  * \t   *  *  \t  *   *\n'
      '*****  \t  *    *\t  ******\t*********\n'
      '*    * \t *      *\t *      *\t*       *\n'
      '******\t*        *\t*        *\t*       *\n')

#5.
print('Escape sequences:')
print('\\a\tBell (alert)')
print('\\b\tBackspace')
print('\\n\tNew line')
print('\\t\tHorizontal tab')
print('\\\\\tBackslash \\')
print('\\”\tDouble quotation mark “')
print('\\’\tSingle quotation mark ‘')

#6.
x = int(input("Введите число: "))
y = int(input("Введите число: "))
summ = x + y
division = x // y
balance = x % y
power = x ** y
print(x, y)
print('Сумма {} и {} = {}'.format(x, y, summ))
print('Результат деления {} и {} = {}'.format(y, x, division))
print('Остаток от деления {} и {} = {}'.format(y, x, balance))
print('Степень числа {} и {} = {}'.format(x, y, power))

#7.
a = 5
b = 10
c = 20
print(a + b + c)  #35

#8.
K1 = int(input("Введите первый катет: "))
K2 = int(input("Введите второй катет: "))
print('Площадь: {}'.format(K1 * K2 / 2))

