n = int(input())
lis = []
for i in range(n):
    lis.append(list(map(int, input().split())))
vals = []
for i in range(n):
    count = 0
    for j in range(n):
        if j == i: continue
        if lis[i] == lis[j]: continue
        if (lis[i][0] < lis[j][0] and lis[i][1] < lis[j][1]):
            count += 1
    vals.append(count)
for i in range(n):
    print(vals[i]+1, end = ' ')