n, a, x, y = map(int, input().split())

total = 0

if n <= a:
    total = n * x
else:
    total += a * x
    total += (n - a)*y
print(total)