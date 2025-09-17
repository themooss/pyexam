# ANSWER: 1047

c = 0
for line in open('task9/23555/23555.txt'):
    a = [int(x) for x in line.split()]
    p3 = [x for x in a if a.count(x) == 3]
    p2 = [x for x in a if a.count(x) == 2]
    np = [x for x in a if a.count(x) == 1]
    if (len(p3) != 0 and len(p2) != 0 and len(np) != 0)\
    and len(p3) == 3 and len(p2) == 2 and len(np) == 2\
        and max(p3[0], p2[0]) > max(np):
        c += 1
print(c)
         