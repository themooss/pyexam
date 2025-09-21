# ANSWER: 334

c = 0
for line in open('task9/MMigunov2026/MMigunov2026.txt'):
    a = [int(x) for x in line.split()]
    p3 = [x for x in a if a.count(x) == 3]
    p2 = [x for x in a if a.count(x) == 2]
    np = [x for x in a if a.count(x) == 1]
    s = sorted(a)[::-1]

    if (p3 == 3 and p2 == 2 and np == 2) or\
        (s[0] + s[1] <= s[-1] + s[-2] + s[-3]):
        c += 1
print(c)