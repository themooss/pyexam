#ANSWER: 17

res = []
i = 1
for line in open('C:/Users/Admin/Documents/pyexam/task9/23268/23268.txt'):
    a = [int(x) for x in line.split()]
    p2 = [x for x in a if a.count(x) == 2]
    np = [x for x in a if a.count(x) == 1]
    if (len(p2) > 0 and len(np) > 0 and len(p2) == 4 and len(np) == 3) and sum(p2) / len(p2) < max(np):
        res.append(i)
    i += 1
print(res[0])
