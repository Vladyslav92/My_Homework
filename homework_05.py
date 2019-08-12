#1 Задачка.
string = "123456789"
print(string[2])
print(string[-2])
print(string[:5])
print(string[:-2])
print(string[::2])
print(string[1::2])
print(string[::-1])
print(string[::-2])
print(len(string))

#2 Задачка.
string = "Everyone Loves Python"
print("В строке", string.count(' ') + 1, "слова")

#3 Задачка.
hello = "Hello World!"
a = hello.split()
a[-1], a[0] = a[0], a[-1]
print(' '.join(a))

#4 Задачка.
string = "Hello Hero!"
string = string[:string.find('H')] + string[string.rfind('H') + 1:]
print(string)