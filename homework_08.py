# Задача 1.
def shift(number, position, direction=False):
    if position < 0:
        print(direction)
    else:
        for i in range(position):
            number.insert(0, number.pop())


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums)

shift(nums, int(input("На сколько сдвинутся: ")))
print(nums)

# Задача 2.
import string
digs = string.digits + string.ascii_uppercase


def convert_function(num, to_base):
    if num < 0:
        sign = -1
    elif num == 0:
        return digs[0]
    else:
        sign = 1
    num *= sign
    digits = []
    while num:
        digits.append(digs[int(num % to_base)])
        num = int(num / to_base)
    if sign < 0:
        digits.append('-')
    digits.reverse()
    return ''.join(digits)


print(convert_function(int(input("Введите число: ")), int(input("В какую систему переводим (2-36): "))))
