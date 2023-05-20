n = int(input())
lis = []
for i in range(n):
    lis.append(list(map(int, input().split())))
lis.sort(key = lambda x: (x[0], x[1]))
for i in range(n):
    print(lis[i][0], lis[i][1])