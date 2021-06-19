N = int(input())

N *= 1.08

if int(N) < 206:
    print("Yay!")
elif int(N) == 206:
    print("so-so")
else:
    print(":(")