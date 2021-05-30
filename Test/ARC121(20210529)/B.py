N = int(input())

dog = []

for n in range(2 * N):
    a, c = input().split()
    dog.append([int(a),c])

dog_sort = sorted(dog)
color = []

for i in dog:
    color.append(i[1])

dist = 0
max_num = 1
min_num = -2

RGB = ['R', 'G', 'B']
ar = []

def my_index_multi(l, x):
    a = []
    for x_ in l:
        if x_[1] == x:
            a.append(x_[0])
    return a

if(color.count('R')%2 == 0 and color.count('G')%2 == 0 and color.count('B')%2 == 0):
    print("0")
else:
    for i in range(3):
        if(color.count(RGB[i])%2 != 0):
            ar.append(my_index_multi(dog_sort, RGB[i]))

    min = 1000000

    for i1 in range(len(ar[0])):
        for i2 in range(len(ar[1])):
            dist = abs(ar[0][i1]-ar[1][i2])
            if(dist < min):
                min = dist
    print(min)

# while len(dog_sort) != 0:
#     if(dog_sort[0][1] == dog_sort[-1][1]):
#         dist += dog_sort[0][0] - dog_sort[-1][0]
#         del dog_sort[0]
#         del dog_sort[-1]
#     else:
#         max_num += 1
#         while(1):
#             if(dog_sort[max_num][1] != dog_sort[min_num][1]):
#                 dis1 = dog_sort[max_num][0] - dog_sort[-1][0]
#                 mx = max_num
#                 max_num = 1
#                 break
#             else:
#                 max_num += 1
#         while(1):
#             if(dog_sort[max_num][1] != dog_sort[min_num][1]):
#                 dis2 = dog_sort[0][0] - dog_sort[min_num][0]
#                 mn = min_num
#                 break
#             else:
#                 min_num -= 1
        
#         if(dis1 < dis2):
#             dist += dog_sort[0][0] - dog_sort[mn][0]
#             del dog_sort[0]
#             del dog_sort[mn]
#         else:
#             dist+= dog_sort[mx][0] - dog_sort[-1][0]
#             del dog_sort[mx]
#             del dog_sort[-1]
#     if(dog_sort.count('R') == len(dog_sort) or dog_sort.count('B') == len(dog_sort) or dog_sort.count('G') == len(dog_sort) ):
#         dist = 0
#         break