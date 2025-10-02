# ANSWER: 13738

c = 0
for line in open('C:/Users/Admin/Documents/github/pyexam/task9/LShastin2026/txt'):
    a = [int(x) for x in line.split()]
    np = [x for x in a if a.count(x) == 1]
    notmaxmin = [x for x in a if x != min(a) and x != max(a)]
    if len(set(np)) == 5 and ((min(a) + max(a)) <= sum(notmaxmin)):
        c += 1
print(c)