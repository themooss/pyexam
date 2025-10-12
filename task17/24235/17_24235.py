# ANSWER: 3 763482720

with open('17_24235.txt') as file:
    data = [int(x) for x in file.readlines()]

max4 = max([x for x in data if 999 < x < 10000])
c = 0
s = 100000000000000000000000000000000000000000000000
r = []
def ch(n1, n2):
    return (int(999 < abs(n1) < 10000) + int(999 < abs(n2) < 10000)) == 1

for i in range(0, len(data)-1):
    if ch(int(data[i]), int(data[i+1])) and int(data[i]) * int(data[i+1]) % max4 == 0:
        c += 1
        r.append(int(data[i]) * int(data[i+1]))
print(c, abs(min(r)))