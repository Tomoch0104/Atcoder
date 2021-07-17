N = int(input())

C = list(map(int, input().split()))

C.sort()

total = 1

threth = 10**9+7

for c in range(len(C)):
    if c + 1 <= C[c]:
        if threth < total:
            total = total % threth
        total *= C[c] - c
    else:
        total = 0
        break

print(total%(threth))

