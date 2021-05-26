# 自分の回答

# A,B,W = map(float, input().split())

# W *= 1000

# max_n = int(W/A)
# min_n = int(W/B)

# max_count = 0
# min_count = 0

# for a_w in range(int(A),int(B)+1):
#     for b_w in range(int(A), int(B)+1):
#         if(a_w < b_w):
#             for b in range(max_n+1):
#                 for a in range(max_n-b+1):
#                     if min_n <= (a+b):
#                         Sum = a*a_w + b*b_w
#                         if(W == Sum):
#                             if(min_count == 0):
#                                 min_count = a + b
#                             max_count = a + b

# # for b in range(max_n+1):
# #     for a in range(max_n+1):

# if(max_count == 0 and min_count == 0):
#     print("UNSATISFIABLE")
# else:
#     print(max_count,min_count)


import math

a,b,w=map(int,input().split())
upper=int(math.floor(1000*w/a))
lower=int(math.ceil(1000*w/b))
if lower>upper:
    print("UNSATISFIABLE")
else:
    print(lower,upper)