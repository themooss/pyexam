from itertools import product
#this is my practise file of task number 8

def task8_23439_1():
    s = sorted('АЛГОРИТМ')
    i = 1
    for l1 in s:
        for l2 in s:
            for l3 in s:
                for l4 in s:
                    for l5 in s:
                        r = l1+l2+l3+l4+l5
                        if (l1 != 'Т' or l1 != 'Р') and (r.count('И') >= 2) and (i % 2 == 0):
                            print(i)
                        i += 1

def task8_21407_2():
    c = 0
    for i in map(''.join, product(sorted('ДГИАШЭ'), repeat=5)):
        if (i[0] != 'А' and i[0] != 'И' and i[0] != 'Э') and (i[-1] != 'Д' and i[-1] != 'Г' and i[-1] != 'Ш'):
            c += 1
    print(c)
def task8_23554_3(): #8626
    c = 1
    for i in map(''.join, product(sorted('АЛГОРИТМ'), repeat=5)):
        if c % 2 == 0 and i[0] != 'А' and i[0] != 'Г' and i.count('Р') >= 2:
            print(c)
            break
        c += 1

def task8_19240_4(): #6406
    n = 1
    m = []
    for i in map(''.join, product(sorted('январь'), repeat = 5)):
        if i[0] != 'я' and i.count('ь') <= 1 and 'яя' not in i:
            m.append([n, i])   
        n += 1
    print(max(m))    

def task8_MMigunov2026_5(): #-296785
    c = 1
    att_i = 0
    l = 0
    for i in map(''.join, product(sorted('тесак'), repeat=8)):
        f = 'тт' not in i and 'ее' not in i\
    and 'сс' not in i and 'аа' not in i\
        and 'кк' not in i
        if i == 'аттестат':
            att_i = c
        if 'тесак' in i and f:
            l = c
            print(att_i - l)
        c += 1
    else:
        print('--------------')
        print(att_i - l)
def task8_23961_6(): #2499
    c = 1
    for i in map(''.join, product(sorted('КОТИА'), repeat=5)):
        if c % 2 != 0 and (i[0] != 'К' and i[0] != 'Т') and i.count('О') == 2:
            print(c)
        c += 1
    else:
        print('----------') 

def task8_DBahtiev_7(): #24351
    n = 1
    r = 0
    for i in map(''.join, product(sorted('БУРАТИНО'),repeat=5)):
        f1 = len(i) == len(set(i))
        f2 = i[0] not in ['У', 'А', 'И', 'О'] and i[-1] not in ['У', 'А', 'И', 'О']
        if f1 and f2 and n % 2 != 0:
            print(n)
        n += 1
    print(r)
task8_DBahtiev_7()