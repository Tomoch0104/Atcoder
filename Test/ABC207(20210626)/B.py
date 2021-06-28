A, B, C, D = map(int, input().split())

count = 0
C_ = 0

if B < C*D: 
    while(C_*D < A):
        A += B
        C_ += C
        count += 1
else:
    count = -1

print(count)