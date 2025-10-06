from string import printable
from sys import set_int_max_str_digits

set_int_max_str_digits(10000)


def sys(s: int, c: int) -> str:
    res = ''
    while s > 0:
        res = str(s % c) + res
        s //= c
    return res


def task14_20284_1():
    for x in range(0, 42):
        a = 19 * 42 ** 4 + 5 * 42 ** 3 + 6 * 42 ** 2 + 9 * 42 ** 1 + x * 42 ** 0
        a += 1 * 42 ** 3 + x * 42 ** 2 + 18 * 42 ** 1 + 10 * 42 ** 0
        if a % 155 == 0:
            print(x, a // 155)


def task14_21413_2():
    for x in printable[:21]:
        a = int(f'82934{x}2', 21) + int(f'2924{x}{x}7', 21) + int(f'67564{x}8', 21)
        if a % 20 == 0:
            print(x, a // 20)


def task14_23560_3():
    for x in range(1, 2401):  # 2394
        n = 7 * 9 ** 210 + 6 * 9 ** 110 - x
        if sys(n, 9).count('0') == 100:
            print(x, sys(n, 9).count('0'))


def task14_23560_3():  # 266249847
    for x in printable[:25]:
        a = int(f'11353{x}12', 25) + int(f'135{x}21', 25)
        if a % 24 == 0:
            print(x, a // 24)


def task14_MMigunov2026_4():  # 614
    s = -100
    xs = 0
    for x in range(1, 1078):
        n = 7 ** 77 + 7 ** 33 - x
        if str(n).count('0') > s:
            s = str(n).count('0')
            xs = x
    print(s, xs)


def task14_23967_5():
    for x in range(1, 5001):
        p = 7 * 13 ** 180 + 5 * 13 ** 120 - x
        n = sys(p, 13)
        if n.count('0') == 60:
            print(x)


def task14_LShastin2026_6():  # 20
    n = 5 * 729 ** 2024 + 3 * 243 * 1413 - 7 * 81 ** 169 - 2 * 9 ** 107 + 3017
    print(int(sys(n, 27)) // 26)
    print(sum(int(i) for i in '2100000000000000000000000000000000000000000000000000000000000000000012513320'))


def task14_24086_7(): # 233
    c = 0
    for x in range(1, 3001):
        n = sys(5 * 7 ** 156 + 3 * 7 ** 10 - x ** 31, 7)
        if n.count('0') == 15:
            print(x)
            c += 1
    print(c)


