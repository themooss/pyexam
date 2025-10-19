#ANSWER: 42

for line in open('24227.txt'):
    a = [int(x) for x in line.split()]
    np = [x for x in a if a.count(x) == 1]
    chn = [x for x in a if x % 2 == 0]
    minn = min(a)
    if len(np) == 5 and len(chn) == 3 and sum(chn) / len(chn) == minn * 2:
        print(sum(a))
        break