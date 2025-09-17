from string import printable

def sys(s, c):
    res = ''
    while s > 0:
        res = str(s % c) + res
        s //= c
    return res

def task14_20284_1():
    for x in range(0, 42):
        a = 19*42**4 + 5*42**3 + 6*42**2 + 9*42**1 + x*42**0
        a += 1*42**3 + x*42**2 + 18*42**1 + 10*42**0
        if a % 155 == 0:
            print(x, a // 155)

def task14_21413_2():
    for x in printable[:21]:
        a = int(f'82934{x}2', 21) + int(f'2924{x}{x}7', 21) + int(f'67564{x}8', 21)
        if a % 20 == 0:
            print(x, a // 20)

def task14_23560_3():
    for x in range(1, 2401): #2394
        n = 7 * 9 ** 210 + 6 * 9 ** 110 - x
        if sys(n, 9).count('0') == 100:
            print(x, sys(n, 9).count('0'))

def task14_23560_3(): # 266249847
    for x in printable[:25]:
        a = int(f'11353{x}12', 25) + int(f'135{x}21', 25)
        if a % 24 == 0:
            print(x, a // 24)
task14_23560_3()