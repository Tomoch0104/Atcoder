import numpy as np

N, Q = map(int, input().split())

A = list(map(int, input().split()))
A.sort()

K_list = []

# def binary_search(A_list, K):
#     len_A = len(A_list)
#     if len_A == 1:
#         return A_list[0]
#     else:
#         a = len_A%2
#         half = int(len_A/2)
#         if A_list[half] < K:
#             return binary_search(A_list[:half], K)
#         elif K < A_list[half]:
#             return binary_search(A_list[half:], K)
#         else:
#             return A_list[half]


def getNearestValue(list, num):
    idx = np.abs(np.asarray(list) - num).argmin()
    return list[idx]



# def calc(k):
#     try:
#         return A.index(k)
#     except ValueError:
#         return calc(k+1)
    
def ind(k,a):
    if(k+a < len(A)):
        if k + a + 1 < A[a+1]:
            return k + a
        else:
            return ind(k,a+1)
    else:
        return k + len(A)

for q in range(Q):
    K = int(input())
    if K < A[0]:
        K_list.append(K)
    elif K > A[-1]:
        K_list.append(len(A) + K)
    else:
        count = 0
        a = getNearestValue(A,K)
        if(A[a] > K):
            a -= 1
        if(K + a + 1 < A[a + 1]):
            K_list.append(K+a+1)
        else:
            a = ind(K,a)
            K_list.append(a)

for q in range(Q):
    print(K_list[q])