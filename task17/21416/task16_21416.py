with open('task17/21416/17_21416.txt') as file:
    data = file.readlines()

m = -100_001
c = 0
negative_sum = sum([int(i) for i in data if int(i) < 0])

def f(n1, n2, n3):
    s = [int(n1), int(n2), int(n3)]
    return min(s) * max(s) > negative_sum

for i in range(0, len(data) - 2):
    if f(data[i], data[i+1], data[i+2]):
        c += 1
        m = max(m, sum([int(data[i]), int(data[i+1]), int(data[i+2])]))

print(c)
print(m)
