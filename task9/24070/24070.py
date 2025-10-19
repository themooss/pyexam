#ANSWER: 13728

c = 0
for line in open('24070.txt'):
    a = [int(x) for x in line.split()]
    np = [x for x in a if a.count(x) == 1]
    max_a = max(a)
    min_a = min(a)
    not_min_not_max = [x for x in a if x != min(a) and x != max(a)]
    if len(np) == 5 and (max_a + min_a) <= sum(not_min_not_max):
        c += 1
print(c)