# # 解法1

# t, N = map(int, input().split())

# def f(x):
#     return (100 + t) * x // 100

# ok = 0
# ng = 100 * N

# while ok + 1 < ng:
#     x = (ok + ng) // 2
#     if f(x) - x < N:
#         ok = x
#     else:
#         ng = x

# ans = f(ok) + 1
# print(ans)


# 解法2
import numpy as np

t, N = map(int, input().split())
P = 100 + t

A = np.ones(P, np.bool)
for x in range(100):
    A[P * x // 100] = 0

# P以下で、税込み価格にならない金額
B = np.where(A)[0]
# 何回目の周期の何番目か
q, r = divmod(N-1, t)
ans = P * q + B[r]
print(ans)