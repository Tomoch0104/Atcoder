N, K = map(int, input().split())

friend = []
now_village = 0
state = 0

for n in range(N):
    A ,B = map(int, input().split())
    friend.append([A, B])

fri_sort = sorted(friend)
# friend.sort()

for f in fri_sort:
    next_max = now_village + K
    if(f[0] <= next_max):
        K += (f[1] - (f[0] - now_village))
        now_village = f[0]
    else:
        state = 1
        break


if state==0:
    next_max = now_village + K

if(next_max <= 10**100):
    print(next_max)
else:
    print(10**100)