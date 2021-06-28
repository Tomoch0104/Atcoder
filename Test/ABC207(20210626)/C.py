N = int(input())

t = []
count = 0

for _ in range(N):
    t.append(list(map(int, input().split())))

for i in range(1, len(t)):
    for j in range(i):
        if not (t[j][2] <= t[i][1] or t[i][2] <= t[j][1]):
            count += 1
        else:
            if t[i][1] == t[j][2]:
                if (t[i][0] == 2 or t[i][0] == 1) and (t[j][0] == 3 or t[j][0] == 1):
                    count += 1
            elif t[i][2] == t[j][1]:
                if (t[i][0] == 3 or t[i][0] == 1) and (t[j][0] == 2 or t[j][0] == 1):
                    count += 1
        

print(count)