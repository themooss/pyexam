# ANSWER: 87 184328

with open('task17/23563/17_23563.txt') as file:
    data = file.readlines()
mpe = min([int(x) for x in data if int(x) > 0 and int(x) % 35 == 0])
ms = -200001
c = 0

def isElementsNotEqual(n1, n2):
    return int(n1) != int(n2)

for i in range(0, len(data) - 1):
    if abs(int(data[i]) - int(data[i+1])) % mpe == 0 and isElementsNotEqual(int(data[i]), int(data[i+1])):
        c += 1
        ms = max(ms, (int(data[i]) + int(data[i+1])))
print(c, ms)       