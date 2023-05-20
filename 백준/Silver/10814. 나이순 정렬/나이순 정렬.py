N = int(input())
val = []
for i in range(N):
    chk = input().split()
    chk[0] = int(chk[0])
    chk.append(i)
    val.append(chk)
val.sort(key = lambda x: (x[0], x[2]))
for i in range(N):
    print(val[i][0], val[i][1])