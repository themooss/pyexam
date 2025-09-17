from math import ceil

#this is my practise file of task number 8

def task11_23442_1():
    alphabet = 10 + 52 + 963 
    c = 2000
    m = 693 * 1024 * 8
    l = m / c
    print(l)
    print({alphabet})
    print(l / 11)

def task11_21410_2():
    l = 257
    c = 295_740
    mem = 33 * 1024 * 1024 * 8
    p = l * c
    res1 = mem // p
    print(res1)

def task11_23557_3(): #896
    a = 500 + 52 + 10
    i = 10
    c = 45_877
    mem = 49 * 1024 * 1024 * 8
    print(ceil(mem / c / i))

def task11_19243_4(): # 5.19 -> 6 -> 2^6 = 64(min = 33)
    l = 377
    c = 23_155
    mem = 5536 * 1024 * 8
    print((mem // c) / 377)
task11_19243_4()