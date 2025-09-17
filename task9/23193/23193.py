#ANSWER: 10493

res = []
i = 1
for line in open('task9/23193/23193.txt'):
    a = [int(x) for x in line.split()]
    n3 = [x for x in a if a.count(x) == 3]
    np = [x for x in a if a.count(x) == 1]
    if len(n3) == 3 and len(np) == 3 and n3[0] > (sum(np) / len(np)):
        res.append(i)
    i +=1
print(res)