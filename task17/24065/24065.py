# ANSWER: 19 10200

with open('17_24065.txt') as file:
    data = [int(x) for x in file.readlines()]

ms = 0
c = 0
mint = min([x for x in data if 99 < x < 1000])

def ch(n1, n2) -> bool:
    return int(99 < n1 < 1000) + int(99 < n2 < 1000) == 1

for i in range(0, len(data)-1):
    if ch(int(data[i]), int(data[i+1])) and ((int(data[i]) + int(data[i+1])) % mint == 0):
        c += 1
        ms = max(ms, int(data[i]) + int(data[i+1]))
print(c, ms)