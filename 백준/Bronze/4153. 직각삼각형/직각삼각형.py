while True:
    a = list(map(int, input().split()))
    if a[0] == 0 and a[1] == 0 and a[2] == 0:
        break
    maxi = a.index(max(a))
    hap = 0
    for i in range(3):
        if maxi != i:
             hap += (a[i]**2)
    if hap == (a[maxi]**2):
        print("right")
    else: print("wrong")