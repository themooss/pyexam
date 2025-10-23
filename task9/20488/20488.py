# ANSWER: 1382

c = 0
for line in open('20488.txt'):
    a = [int(x) for x in line.split()]
    np = [x for x in a if a.count(x) == 1]
    p = [x for x in a if x not in np]
    f1 = len(np) < 7
    f2 = max(a) not in p
    f3 = (sum(np) >= 3 * sum(p))
    if f1 and f2 and f3:
        c += 1
print(c)
