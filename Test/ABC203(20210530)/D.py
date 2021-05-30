import numpy as np

N, K = map(int,input().split())

A = []

for n in range(N):
    a_ver = list(map(int, input().split()))
    A.append(a_ver)

min_median = 10**9
median_num = int((K**2-1)/2)

for h in range(len(A)-(K-1)):
    for l in range(len(A[0])-(K-1)):
        k_lect = np.array(A)[h:h+K, l:l+K]
        sort_array = np.sort(k_lect.reshape(-1))
        min_sub = sort_array[median_num]
        if(min_sub < min_median):
            min_median = min_sub

print(min_median)