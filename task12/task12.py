
#this is my practise file of task number 12

def task12_23474_1():
    for n in range(3, 4000):    
        s = '1' + '2' * n
        while '12' in s or '312' in s or '222' in s:
            if '12' in s:
                s = s.replace('12', '2', 1)
            if '312' in s:
                s = s.replace('312', '21', 1)
            if '222' in s:
                s = s.replace('222', '311', 1)
        if s.count('1') == 3:
            print(n)

def task12_21411_2():
    for n in range(3, 10001):
        s = '3' + '1' * n
        while '31' in s or '211' in s or '1111' in s:
            if '31' in s:
                s=s.replace('31', '1', 1)
            if '211' in s:
                s=s.replace('211', '13', 1)
            if '1111' in s:
                s=s.replace('1111', '2', 1)
        if sum([int(i) for i in s]) == 15:
            print(n)

def task12_23558_3(): #40
    ms = -100000
    for n in range(3, 10001):
        s = '4' + '2' * n
        while '42' in s or '822' in s or '222' in s:
            if '42' in s:
                s=s.replace('42', '2', 1)
            if '822' in s:
                s=s.replace('822', '24', 1)
            if '222' in s:
                s=s.replace('222', '8', 1)
        if sum([int(x) for x in s]) > ms:
            ms = sum([int(x) for x in s])
    print(ms)

def task12_19244_4(): #37
    for n in range(4, 100):
        s = '1' + '2' * n
        while '12' in s or '322' in s or '222' in s:
            if '12' in s:
                s=s.replace('12', '2', 1)
            if '322' in s:
                s=s.replace('322', '21', 1)
            if '222' in s:
                s=s.replace('222', '3', 1)
        if sum(int(x) for x in s) == 15:
            print(n, s)
            break


def task12_23818_5(): # 1, это машина тьюринга, решал на бумаге
    pass
    # идея: у нас лишь одна единица, перед ней 799 нулей, а то, что дальше, нас не волнует