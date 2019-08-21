def figure_A ():
    left = 15
    right = 1
    L = 3
    R = 15
    C = 21
    for i in range(7):
        print(' ' * left, '* ' * right)
        if i != 6:
            left -= 2
            right += 2
    for i in range(5):
        L += 2
        R -= 2
        C -= 4
        print(' ' * L, '*', ' ' * C, '*')
    print(' ' * 15, '*')


figure_A()
print()


def figure_B ():
    left = 15
    right = 1
    L = 3
    R = 4
    RC = 4
    for i in range(7):
        print(' ' * left, '* ' * right)
        if i != 6:
            left -= 2
            right += 2
    for i in range(4):
        L += 2
        R -= 1
        RC -= 1
        print(' ' * L, '* ', '  ' * R, '*', '  ' * RC, ' *')
    print(' ' * 13, '* * *')
    print(' ' * 15, '*')


figure_B()
