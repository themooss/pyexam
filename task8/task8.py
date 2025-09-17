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
task8_19240_4()