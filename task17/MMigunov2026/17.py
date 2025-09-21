# ANSWER: 13 801833

with open('task17/MMigunov2026/17.txt') as file:
    data = [int(x) for x in file.readlines()]

c = 0
m = -1_000_001
me = max([x for x in data if 9999 < x < 100000 and x % 10000 == 2025])

def ch(n1, n2):
    return int((9999 < abs(n1) < 100000 and abs(n1) % 10000 == 2026)) + int(( 9999 < abs(n2) < 100000 and abs(n2) % 10000 == 2026))

for i in range(0, len(data) - 1):
    if ch(int(data[i]), int(data[i+1])) == 1 and int(data[i]) + int(data[i+1]) > me:
        c += 1
        m = max(m, int(data[i]) + int(data[i+1]))  
print(c, m)