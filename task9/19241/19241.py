# ANSWER: 17975

n = 1
for line in open('task9/19241/19241.txt'):
    a = [int(x) for x in line.split()]
    p3 = [x for x in a if a.count(x) == 3]
    p1 = [x for x in a if a.count(x) == 1]
    if len(p3) == 6 and len(p1) == 1 and (sum(p3)  / len(p3)) < p1[0]:
        print(n)
        print(p3, sum(p3)  / len(p3) ,p1)
    n += 1
print('end') 