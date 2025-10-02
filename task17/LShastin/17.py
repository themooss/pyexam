# ANSWER: 18 8066

with open('C:/Users/Admin/Documents/github/pyexam/task17/LShastin/17.txt') as file:
    data = [int(x) for x in file.readlines()]

ma = -1
c = 0
mi = min([x for x in data if 99 < x < 1000 and x % 10 == 9])

def ch(n1, n2):
    return (int(9 < int(n1) < 100) + int(9 < int(n2) < 100)) >= 1

for i in range(0, len(data)-1):
    if ch(data[i], data[i+1]) and (int(data[i]) + int(data[i+1])) % mi == 0:
        c += 1
        ma = max(ma, (int(data[i]) + int(data[i+1])))

print(c, ma)
