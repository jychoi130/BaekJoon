n = int(input())
lis = []
for i in range(n):
    a = list(map(int, input().split()))
    a[0],a[1] = a[1], a[0]
    lis.append(a)
lis.sort(key = lambda x: (x[0], x[1]))
for i in range(n):
    print(lis[i][1], lis[i][0])