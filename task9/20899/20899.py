c = 0
for line in open('task9/20899/20899.txt'):
    a = [int(x) for x in line.split()]
    mx = set([x for x in a if x == max(a)])
    mn = [x for x in a if x <= max(a)]
    pr = [x for x in a if a.count(x) == 2]
    if list(mx)[0] < sum(mn) and len(pr) == 2:
        c += 1
        #print(a)
       # print(mx, sum(mn), pr)
      #  break
print(c)