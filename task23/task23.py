def task23_LShastin2026_1(start, end):
    if start > end or start == 22:
        return 0
    if start == end:
        return 1
    return task23_LShastin2026_1(start - 2, end) \
        + task23_LShastin2026_1(start - 5, end) \
        + task23_LShastin2026_1(start // 2, end)


def task23_23567_2(x, y):  # 72
    if x <= y:
        return x == y
    return task23_23567_2(x - 2, y) + task23_23567_2(x // 2, y)


def task23_23380_3(x, y):  # 792
    if x >= y or x == 10:
        return x == y
    return task23_23380_3(x + 1, y) + task23_23380_3(x + 2, y) + task23_23380_3(x * 2, y)


def task23_23280_4(x, y):  # 69
    if x <= y or x == 8:
        return x == y
    return task23_23280_4(x - 1, y) + task23_23280_4(x - 4, y) + task23_23280_4(x // 3, y)


def task23_23205_5(x, y):  # 212
    if x <= y or x == 13:
        return x == y
    return task23_23205_5(x - 1, y) + task23_23205_5(x - 2, y) + task23_23205_5(x // 3, y)


def task23_21907_6(x, y):  # 360
    if x >= y or x == 8:
        return x == y
    return task23_21907_6(x + 1, y) + task23_21907_6(x + 2, y) + task23_21907_6(x * 2, y)


def task23_21716_7(x, y):  # 324
    if x >= y or x == 56:
        return x == y
    return task23_21716_7(x + 3, y) + task23_21716_7(x + 7, y) + task23_21716_7(x * 3, y)


def task23_21604_8(x, y):  # 264
    if x <= y or x == 24:
        return x == y
    return task23_21604_8(x - 1, y) + task23_21604_8(x - 4, y) + task23_21604_8(x // 2, y)


def task23_21420_9(x, y):  # 174034068
    if x >= y or x == 35:
        return x == y
    return task23_21420_9(x + 1, y) + task23_21420_9(x + 2, y) + task23_21420_9(x * 2, y)


def task23_20967_10(x, y):  # 9540
    if x <= y or x == 15:
        return x == y
    return task23_20967_10(x - 2, y) + task23_20967_10(x - 3, y) + task23_20967_10(x // 3, y)
