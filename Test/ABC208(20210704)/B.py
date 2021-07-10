P = int(input())

count = 0

def kai(i):
    c = 1
    for j in range(1,i+1):
        c *= j
    return c

for i in range(10,0,-1):
    c = kai(i)
    count += int(P/c)
    P = P % c

print(count)