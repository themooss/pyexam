# ANSWER: 72
res_c = 0
res_s = 0
c = 1
for line in open('task9/23962/23962.txt'):
    a = [int(x) for x in line.split()]
    p2 = [x for x in a if a.count(x) == 2]
    np = [x for x in a if a.count(x) == 1]
    if len(p2) == 2 and len(np) == 4 and sum(np) % p2[0] == 0:
        res_c = c
        res_s = sum(a)
    c += 1
else:
    print(res_c, res_s)