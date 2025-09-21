from sys import setrecursionlimit, set_int_max_str_digits
#this is my practise file of task number 16
setrecursionlimit(1000000)
set_int_max_str_digits(100000)

def task16_23426_1_G(n):
    if n <= 20:
        return n
    if n > 20:
        return task16_23426_1_G(n-2) + 1

def task16_23426_1_F(n):
    return task16_23426_1_G(n-3)

def task16_21415_2_F(n):
    if n <= 5:
        return 1
    if n > 5:
        return n + task16_21415_2_F(n-2)

def task16_23562_3_G(n):
    if n <= 9:
        return 3*n
    if n > 9:
        return task16_23562_3_G(n-2) + 1

def task16_23562_3_F(n): # 24017
    return task16_23562_3_G(n-1)

def task16_19248_4_F(n): #757543052
    if n < 5:
        return n
    if n >= 5:
        return 2 * n * task16_19248_4_F(n-4)

def task16_MMigunov2026_5_F(n):
    if n >= 9876:
        return task16_MMigunov2026_5_F(n + 777)
    if n < 9876:
        return n * 2 + task16_MMigunov2026_5_F(n+2)

def task16_23969_6_G(n):
    if n < 8:
        return 3*n
    if n >=8:
        return task16_23969_6_G(n-3)+2

def task16_23969_6_F(n): #24732
    return 3 * (task16_23969_6_G(n-4) + 5)

print(task16_23969_6_F(12345))