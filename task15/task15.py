# this is my practise file of task number 15


def task15_23561_1_del(x, A):
    return (x % 128 == 0) <= ((x % A != 0) <= (x % 80 != 0))


def task15_23561_1():  # Пересдача 03.07.2025(Уровень: Базовый)
    for A in range(1, 1000):
        if all(task15_23561_1_del(x, A) for x in range(1, 1000)):
            print(A)  # 640


def task15_23374_2_func(A, x, y):
    return (x < A) and (y < 3 * A) or (2 * x + y > 128)


def task15_23374_2():  # Резервный день 19.06.25 (Уровень: Базовый)
    for A in range(1, 1000):
        if all(task15_23374_2_func(A, x, y) for x in range(1, 1000) for y in range(1, 1000)):
            print(A)  # 64
            break


def task15_23274_3_func(A, x, y):
    return (2 * x + y != 110) or (x < y) or (A < x)


def task15_23274_3():  # Основная волна 11.06.25 (Уровень: Базовый)
    for A in range(1000):
        if all(task15_23274_3_func(A, x, y) for x in range(1000) for y in range(1000)):
            print(A)  # 36


task15_23274_3()


def task15_23199_4_func(A, x, y):
    return (x * y > A) or (x > y) or (11 > x)


def task15_23199_4():  # Основная волна 10.06.25 (Уровень: Базовый)
    for A in range(1000):
        if all(task15_23199_4_func(A, x, y) for x in range(1000) for y in range(1000)):
            print(A)  # 120


def task15_23446_5_func(A, x, y):
    return (x > 67) or (y >= x) or ((3 * x) - y < A)


def task15_23446_5():
    for A in range(1, 1000):
        if all(task15_23446_5_func(A, x, y) for x in range(0, 500) for y in range(500)):
            print(A)
            break


def task15_21414_6_func(A, x, y):
    return (5 < y) or (x > 32) or (x + 2 * y < A)


def task15_21414_6():
    for A in range(500):
        if all(task15_21414_6_func(A, x, y) for x in range(500) for y in range(500)):
            print(A)


def task15_19247_8_func(A, x, y):
    return (x - 3 * y < A) or (y > 400) or (x > 56)


def task15_19247_8():  # 54
    for A in range(0, 501):
        if all(task15_19247_8_func(A, x, y) for x in range(1, 501) for y in range(1, 501)):
            print(A)
            break


def task15_MMigunov2026_9():
    z = [x for x in range(27, 50)]
    o = [x for x in range(39, 61)]
    v = [x for x in range(30, 56)]
    z <= ((not (o) and not (o)) <= (not (z) and v))


def task15_DBahtiev2026_10_f(A, x, y):
    return (2 * x * y > A) or (y < x) or (x < 15)


def task15_DBahtiev2026_10():  # 449
    for A in range(1, 1000):
        if all(task15_DBahtiev2026_10_f(A, x, y) for x in range(1, 1000) for y in range(1, 1000)):
            print(A)


def d(n, m):
    return n % m == 0


def t24066_f(x, A):
    return ((not (d(x, A))) <= (not (d(x, 21)))) or ((not (d(x, 35))) <= d(x, 5))


def task15_24066_11():  # 21
    for A in range(1, 500):
        if all(t24066_f(x, A) for x in range(1, 500)):
            print(A)


def task15_24233_12_F(A, x, y): # 25
    return (3 * x + y != 96) or (x <= y) or (A <= x)

def task15_24233_12(): # 25
    for A in range(0, 500):
        if all(task15_24233_12_F(A, x, y) for x in range(0, 500) for y in range(0, 500)):
            print(A)


def task15_24106_13_F(A, x, y):
    return (2 * x * y > A) or (y < x) or (x < 15)

def task15_24106_13(): # 449
    for A in range(1, 1000):
        if all(task15_24106_13_F(A, x, y) for x in range(1, 1000) for y in range(1, 1000)):
            print(A)
task15_24106_13()