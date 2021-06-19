N = int(input())

A = list(map(int, input().split()))

A.sort()
c = 0

for n in range(N-1):
    if A[n+1] - A[n] != 1:
        c = 1

if c==0:
    print("Yes")
else:
    print("No")