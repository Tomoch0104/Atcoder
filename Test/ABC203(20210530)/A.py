a = list(map(int, input().split()))

a.append("0")
state = 3

for i in range(3):
    for j in range(3):
        if(i != j):
            if(a[i] == a[j]):
                for n in range(3):
                    if(i != n and j != n):
                        state = n


print(a[state])