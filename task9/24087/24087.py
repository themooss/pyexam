#ANSWER: 477

n = 1
for line in open('24087.txt'):
    a = [int(x) for x in line.split()]
    p4 = [x for x in a if a.count(x) == 4]
    if len(p4) == 4 and (sum(a) / len(a) >= p4[0]):
        print(sum(a), n)
        break
    n += 1