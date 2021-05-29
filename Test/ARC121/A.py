N = int(input())

n1 = 10**9
n2 = 10**9

x_list = []
y_list = []

for i in range(N):
    x,y = map(int, input().split())
    x_list.append([x,i])
    y_list.append([y,i])

x_new = sorted(x_list)
y_new = sorted(y_list)

new = x_new + y_new

max_ = []

for i in range(2):
    for j in range(2):
        index = [abs(x_new[i][0] - x_new[-1*(j+1)][0]),[x_new[i][1],x_new[-1*(j+1)][1]]]
        max_.append(index)
        index = [abs(y_new[i][0] - y_new[-1*(j+1)][0]),[y_new[i][1],y_new[-1*(j+1)][1]]]
        max_.append(index)

max_a = sorted(max_, reverse=True)

if(max_a[0][1] != max_a[1][1]):
    print(max_a[1][0])
else:
    print(max_a[2][0])