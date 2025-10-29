# ANSWER: 2 87487

with open('17.txt') as file:
    data = [int(x) for x in file.readlines()]

maxabs = 0
max3 = max(x for x in data if 99 < abs(x) < 1000)
c = 0


def ch(n1, n2, n3):
    return int(99 < n1 < 1000) + int(99 < n2 < 1000) + int(99 < n3 < 1000) == 2


for i in range(len(data)-2):
    if ch(int(data[i]), int(data[i+1]), int(data[i+2])) and ((int(data[i]) * int(data[i+1]) * int(data[i+2])) % max3 == 0):
        c += 1
        maxabs = max(abs(maxabs), abs(int(data[i]) + int(data[i+1]) + int(data[i + 2])))
print(c, maxabs)
