# ANSWER: 18 8066

with open('17_24074.txt') as file:
    data = [int(x) for x in file.readlines()]

c = 0
ms = 0

mn = min([x for x in data if 99 < x < 1000 and x % 10 == 9])

def ch(n1, n2):
    return (int(9 < n1 < 100) + int(9 < n2 < 100)) >= 1

for i in range(0, len(data)-1):
    if ch(int(data[i]), int(data[i+1])) and (int(data[i]) + int(data[i+1])) % mn == 0:
        c += 1
        ms = max(ms, int(data[i]) + int(data[i+1]))
print(c, ms)