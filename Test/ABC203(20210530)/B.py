N ,K = map(int, input().split())

room = []

for n in range(1,N+1):
    for k in range(1,K+1):
        k_ = str(k)
        room.append(int(str(n)+k_.zfill(2)))

print(sum(room))