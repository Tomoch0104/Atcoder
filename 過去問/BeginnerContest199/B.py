N = int(input())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

C = min(B) - max(A) + 1 if 0 <= min(B) - max(A) else 0
print(C)