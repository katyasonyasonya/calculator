a = 'да'
print('Привет')
print('Эта программа может выполнять:')
print("сложение - '+'")
print("вычитание - '-'")
print("умножение - '*'")
print("деление - '/'")
print("целочисленное деление - '//'")
print("взятие остатка - '%'")
print("возведение в степень - '**'")
print("квадратный корень числа - '///'")
print("переводить из любой системы счисления в десятичную - '<>'")
print("анализ числа - '^'")
while a == 'да' or a == 'lf':
    v1 = 0
    v2 = 0
    v3 = 0
    v4 = 0
    v5 = 0
    v6 = 0
    v7 = 0
    v8 = 0
    v9 = 0
    v0 = 0
    print('Напиши что ты хочешь от компуктера')
    print('Напиши певрое число')
    x = int(input())
    print('Напиши действие')
    c = input()
    if c == '+' or c == '-' or c == '*' or c == '/' or c == '//' or c == '%' or c == '**':
        print('Напиши второе число')
        y = int(input())
        b = len(str(x))
    elif c == '///' or c == '<>' or c == '^':
        b = len(str(x))
    else:
        print('Ошибка')
        b = len(str(x))
    if c == '+':
        print(x, '+', y, '=', x + y)
    elif c == '-':
        print(x, '-', y, '=', x - y)
    elif c == '*':
        print(x, '*', y, '=', x * y)
    elif c == '/':
        print(x, '/', y, '=', x / y)
    elif c == '//':
        print(x, '//', y, '=', x // y)
    elif c == '%':
        print(x, '%', y, '=', x % y)
    elif c == '**':
        print(x, '**', y, '=', x ** y)
    elif c == '///':
        print(x, '/// =', x ** 0.5)
    elif c == '<>':
        print('я не поняла как это делать, но честно пыталась')
        print('x =', int(x, 2))
    elif c == '^':
        if b == 1:
            print('1) 1 разряд')
        elif b == 2 or b == 4 or b == 3:
            print('1)', b, 'разряда')
        else:
            print('1)', b, 'разрядов')
        t = x
        n = x
        while b != 0:
            if (x % 10) == 1:
                v1 = 1 + v1
            elif (x % 10) == 2:
                v2 = 1 + v2
            elif (x % 10) == 3:
                v3 = 1 + v3
            elif (x % 10) == 4:
                v4 = 1 + v4
            elif (x % 10) == 5:
                v5 = 1 + v5
            elif (x % 10) == 6:
                v6 = 1 + v6
            elif (x % 10) == 7:
                v7 = 1 + v7
            elif (x % 10) == 8:
                v8 = v8 + 1
            elif (x % 10) == 9:
                v9 = v9 + 1
            else:
                v0 = 1 + v0
            b = b - 1
            x = x // 10
        g = 0
        print('2)')
        if v1 != 0:
            if v1 == 2 or v1 == 3 or v1 == 4:
                print('1 =', v1, 'раза')
            else:
                print('1 =', v1, 'раз')
        else:
            g += 1
        if v2 != 0:
            if v2 == 2 or v2 == 3 or v2 == 4:
                print('2 =', v2, 'раза')
            else:
                print('2 =', v2, 'раз')
        else:
            g += 1
        if v3 != 0:
            if v3 == 2 or v3 == 3 or v3 == 4:
                print('3 =', v3, 'раза')
            else:
                print('3 =', v3, 'раз')
        else:
            g += 1
        if v4 != 0:
            if v4 == 2 or v4 == 3 or v4 == 4:
                print('4 =', v4, 'раза')
            else:
                print('4 =', v4, 'раз')
        else:
            g += 1
        if v5 != 0:
            if v5 == 2 or v5 == 3 or v5 == 4:
                print('5 =', v5, 'раза')
            else:
                print('5 =', v5, 'раз')
        else:
            g += 1
        if v6 != 0:
            if v6 == 2 or v6 == 3 or v6 == 4:
                print('6 =', v6, 'раза')
            else:
                print('6 =', v6, 'раз')
        else:
            g += 1
        if v7 != 0:
            if v7 == 2 or v7 == 3 or v7 == 4:
                print('7 =', v7, 'раза')
            else:
                print('7 =', v7, 'раз')
        else:
            g += 1
        if v8 != 0:
            if v8 == 2 or v8 == 3 or v8 == 4:
                print('8 =', v8, 'раза')
            else:
                print('8 =', v8, 'раз')
        else:
            g += 1
        if v9 != 0:
            if v9 == 2 or v9 == 3 or v9 == 4:
                print('9 =', v9, 'раза')
            else:
                print('9 =', v9, 'раз')
        else:
            g += 1
        if v0 != 0:
            if v0 == 2 or v0 == 3 or v0 == 4:
                print('0 =', v0, 'раза')
            else:
                print('0 =', v0, 'раз')
        else:
            g += 1
        if (t % 2) == 0:
            print('3) четное')
        else:
            print('3) не четное')
        d = len(str(t))
        p = 0
        while d != 0:
            d = d - 1
            p = p + t % 10
            t = t // 10
        print('4) сумма цифр =', p)
        if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
            print('5) простое число')
        else:
            print('5) непростое число')
            m = 2
            p = '1'
            while n >= m:
                if n % m == 0:
                    p = p + ', ' + str(m)
                    m += 1
                else:
                    m += 1
            print('делители:', p)
            z = n ** 0.5
            z1 = round(z)
            r = z ** 0.5
            r1 = round(r)
            if z1 ** 2 == n:
                print('6) является полным квадратом числа', z1)
            else:
                print('6) не является полным квадратом')
            if r1 ** 3 == n:
                print('7) является полным кубом числа', r1)
            else:
                print('7) не является полным кубом')
    else:
        print('Ошибка')
    print('Желаете ли вы выполнить еще действие?')
    a = input()
print('Пока')
