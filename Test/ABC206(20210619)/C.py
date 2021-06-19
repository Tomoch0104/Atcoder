import collections

N = int(input())

A = list(map(int, input().split()))
count = 0

l = N-1

if (l) % 2 == 0:
    count = int((N)*l/2)
else:
    count = int((N)*int(l/2) + N/2)

b = -1
A.sort()
i = 0
A_ = set(A)
dis = len(A) - len(A_)
while(dis != 0 and i < N):
    a = A[i]
    c = 1
    if i != N-1:
        while(a == A[i+1]):
            c += 1
            i += 1
            if(i == N-1):
                break
    if c > 1:
        if (c-1) % 2 == 0:
            count -= int((c)*(c-1)/2)
        else:
            count -= int((c)*int((c-1)/2) + c/2)
        dis -= 1
    i += 1

print(count)

# for i in range(N-1):
#     for j in range(i+1,N):
#         if A[i] != A[j]:
#             count += 1

# A_ = set(A)

# l = len(A)

# for i in range(1,l):
#     count += i 

# print(count)

"""
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void){
  int N;
  int count = 0;
  cin >> N;
  vector<int> A(N);
  for (auto& x : A) {
      cin >> x;
  }
  for(int i = 0; i < N-1;i++){
  	for(int j = i+1; j < N; j++){
      if(A[i] != A[j])
        count++;
    }
  }
  printf("%d", count);
  return 0;
}
"""