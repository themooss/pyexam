# ANSWER: 39997

n = 1
res = 1
for line in open('iglin_3.txt'):
    a = [int(x) for x in line.split()]
    nch = [x for x in a if x % 2 != 0]
    minn = min(a)
    maxn = max(a)
    if ((maxn - (sum(a) / len(a))) <= minn) and (sum(nch) % 2 == 0):
        res = n
        print(res)
    n += 1
print(res)