
#this is my practise file of task number 5

def sys(num, ss):
    res = ''
    while num > 0:
        res = str(num%ss) + res
        num //= ss
    return res

def task5_23437_1():
    for n in range(1, 1001):
        n_3 = sys(n, 3)
        if n % 3 == 0:
            n_3 = '1' + n_3 + '02'
        if n % 3 != 0:
            n_3 = n_3 + sys(((n % 3) * 4), 3)
        r = int(n_3, 3)
        if r < 199:
            print(n)

def task5_21404_2():
    for n in range(1, 501):
        b = bin(n)[2:]
        if b.count('1') % 2 == 0:
            b = b + '0'
            b = '10' + b[2:]
        else:
            b = b + '1'
            b = '11' + b[2:]
        r = int(b, 2)
        if r > 480:
            print(n, r)
            break
            
def task5_20896_3():#8
    for n in range(1, 1001):
        b = bin(n)[2:]
        if b.count('0') % 2 == 0:
            b = b + '0'
            b = '10' + b[2:]
        else:
            b = b + '1'
            b = '11' + b[2:]
        r = int(b, 2)
        if r > 19:
            print(n, r)
            
def task5_23551_4(): #6
    for n in range(1, 1001):
        b = bin(n)[2:]
        if n % 2 == 0:
            b = '10' + b
        else:
            b = '1' + b + '01'
        r = int(b, 2)
        if r < 30:
            print(n, r)

def task5_19237_5(): #222
    for n in range(1, 1001):
        t = sys(n, 3)
        if n % 3 == 0:
            t = t + t[-2:]
        else:
            t = t + sys((sum([int(x) for x in t])), 3)
        r = int(t, 3)
        if r % 2 == 0 and r > 220:
            print(r)
            
task5_19237_5()
