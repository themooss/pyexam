#ANSWER: 92 838850571

with open('task17/19249/17_19249.txt') as file:
    data = file.readlines()

c = 0
m = 1 * 10**100
mp = max([int(x) for x in data if 9999 < int(x) < 100000 and int(x) % 100 == 43])

def is_five_digit(n1, n2, n3):
    return (9999 < abs(n1) < 100001 and abs(n1) % 100 == 43) or\
    (9999 < abs(n2) < 100001 and abs(n2) % 100 == 43) or\
    (9999 < abs(n3) < 100001 and abs(n3) % 100 == 43) 

for i in range(0, len(data) - 2):
    if is_five_digit(int(data[i]), int(data[i+1]), int(data[i+2])) >= 1 and\
    int(data[i]) ** 2 + int(data[i+1]) ** 2 + int(data[i+2]) ** 2 <= mp ** 2:
        c += 1
        m = min(m, int(data[i]) ** 2 + int(data[i+1]) ** 2 + int(data[i+2]) ** 2)
print(c, m)