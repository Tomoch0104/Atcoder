N, X = map(int, input().split())

A = list(map(int, input().split()))

a = int(N/2)

b = sum(A) - a

if b <= X:
    print("Yes")
else:
    print("No")