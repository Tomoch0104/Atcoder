A = list(map(int, input().split()))

B = []

for a in range(3):
    for b in range(3):
        if a != b:
            B.append(A[a]+A[b])

B.sort()
print(B[-1])