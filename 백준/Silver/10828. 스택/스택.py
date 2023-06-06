import sys

N = int(input())
lis = [0 for x in range(N+1)]
n = 0

for i in range(N):
    a = sys.stdin.readline().strip()
    if a == "pop":
        if n > 0:
            print(lis[n])
            n -= 1
        else: print("-1")
    elif a == "size":
        print(n)
    elif a == "empty":
        if n == 0:
            print("1")
        else: print("0")
    elif a == "top":
        if n > 0:
            print(lis[n])
        else: print("-1")
    else:
        b = a.split()
        n += 1
        lis[n] = b[1]