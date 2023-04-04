a = int(input())
for i in range(a):
    hap = 0
    x = input()
    chk = 0
    for j in x:
        if j == 'O':
            chk += 1
            hap += chk
        else: chk = 0
    print(hap)