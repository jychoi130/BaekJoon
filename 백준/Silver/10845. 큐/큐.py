import sys

N = int(input())
lis = [0 for x in range(N+1)]
n = 0
chk = 1
end = 0

for i in range(N):
    a = sys.stdin.readline().strip()
    #a = input()
    if a == "pop":
        if n > 0:
            print(lis[chk])
            n -= 1
            if n == 0:
                chk = 1
                end = 0
            else: chk += 1
        else: 
            print("-1")
    elif a == "size":
        print(n)
    elif a == "empty":
        if n == 0:
            print("1")
        else: print("0")
    elif a == "front":
        if n > 0:
            print(lis[chk])
        else: print("-1")
    elif a == "back":
        if n > 0:
            print(lis[end])
        else: print("-1")
    else:
        b = a.split()
        n += 1
        end += 1
        lis[end] = b[1]