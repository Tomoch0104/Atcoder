import numpy as np

N = int(input())
A = []

O = np.ones(N)

for i in range(N):
    A.append(int(input()))

neg_num = int((N+1)/2)


for i in range(neg_num):
    s = []
    a = (i-1) * 2
    for n in range(len(N)):
        if(i <= n):
            if(n < a):
                s.append(len(N)-a)
            s.append(1)
        else:
            s.append(-1)

# for i in range(neg_num+1):
#     for a in range(i):
#         list_ = []
#         list_.append()

# def f(O, q, num):
#     for a in range():
#         for l in range():
#             O += q
#             if(0 < num):
#                 O = f(O, q, num)
#                 num -= 1
#             else:
#                 return O