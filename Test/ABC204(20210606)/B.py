N = int(input())

A = list(map(int, input().split()))

count = 0

for a in A:
    if 10 < a:
        count += a - 10 

print(count)