N, M = map(int, input().split())

flont = []
Back = []

for i in range(N):
    A, B = map(int, input().split())
    if A < B:
        flont.append([A, B])
    else:
        Back.append([A, B])
flont.sort()
Back.sort()

print(flont)
print(Back)

