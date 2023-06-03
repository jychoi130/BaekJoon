n = int(input())

if n == 1 or n == 2:
    print(n)
    
else:
    lis = list(range(1, n + 1))
    s = len(lis) + 1
    del lis[0::2]
    while len(lis) > 1:
        if s % 2 ==  0:
            c = 1
        else: c = 0
        s += (len(lis))
        del lis[c::2]
    print(lis[0])