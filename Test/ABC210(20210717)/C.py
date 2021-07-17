n, k = map(int, input().split())

C = list(map(int, input().split()))
max = 0
index = 0

while index+k <= n:
    c = len(set(C[index:index+k]))
    if max <= c:
        max = c
        index += 1
    else:
        index += (max-c)

print(max)