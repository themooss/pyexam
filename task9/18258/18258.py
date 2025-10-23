# ANSWER: 6937

t = 0
res = []
for line in open('18258.txt'):
    t += 1
    a = [int(x) for x in line.split()]
    np = [x for x in a if a.count(x) == 1]
    p = [x for x in a if x not in np]
    f1 = a == sorted(a)
    f2 = False
    for n in p:
        if sum([int(x) for x in str(n)]) % 2 == 0:
            f2 = True
    if f1 and f2:
        res.append(t)
print(max(res))
