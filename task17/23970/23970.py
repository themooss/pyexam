#ANSWER: 2 14580986

with open('task17/23970/17_23970.txt') as file:
    data = [int(x) for x in file.readlines()]
c = 0
m = 2000000000000000
mxe = max([x for x in data if 99 < x < 1000])

def ch(n1, n2):
    return int(99 < n1 < 1000) + int(99 < n2 < 1000)

for i in range(0, len(data)-1):
    if ch(data[i], data[i+1]) == 1 and int(data[i]) * int(data[i+1]) % mxe == 0:
        c += 1
        m = min(m, int(data[i]) * int(data[i+1]))
print(c, m)