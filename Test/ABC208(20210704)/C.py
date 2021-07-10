N, K = map(int, input().split())

a = list(map(int, input().split()))

if N != 1:
    a_ = sorted(a)
    count = K//N
    K_ = K%N
    threth = a_[K_]
    for A in a:
        if A < threth:
            print(count + 1)
        else:
            print(count)
else:
    print(K)