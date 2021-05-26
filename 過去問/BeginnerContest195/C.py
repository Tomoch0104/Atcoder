N = input()

Count = 0
l = len(N)-1

for i in range(l-l%3,0,-3):
    Count += int(i/3 * (int(N)-10**i + 1))
    N = '9'*i

print(Count)