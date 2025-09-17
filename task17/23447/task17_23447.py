with open('task17/23447/23447.txt') as file:
    data = file.readlines()

maxn39 = max([int(i) for i in data if 999 < int(i) < 10000 and int(i) % 100 == 39])
maxn = 200001
c = 0
s = []


def isFourDigit(i):
    return (len(data[i]) == 4 and len(data[i+1]) != 4) or (len(data[i+1]) == 4 and len(data[i]) != 4)

for i in range(0, len(data) - 1):
    if (int(data[i]) + int(data[i+1])) ** 2 <= maxn39 ** 2 and isFourDigit(i):
        c += 1
        s.append(int(data[i]) + int(data[i+1]))
print(c)
print(max(s))