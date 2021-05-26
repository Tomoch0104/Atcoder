N = int(input())
S = input()
Q  = int(input())

t = True
Out = list(S)

for _ in range(Q):
    T, A, B = map(int, input().split())
    A -= 1
    B -= 1
    if(T == 1):
        if(t):
            Out[A], Out[B] = Out[B], Out[A]
        else:
            if B < N:
                Out[A+N],Out[B+N] = Out[B+N],Out[A+N]
            elif N <= A:
                Out[A-N],Out[B-N] = Out[B-N],Out[A-N]
            else:
                Out[A+N],Out[B-N] = Out[B-N],Out[A+N]
    else:
        if(t):
            t = False
        else:
            t = True

if(t == False):
    Out[:N], Out[N:] = Out[N:], Out[:N]

print(''.join(Out))