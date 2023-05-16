n, m = map(int, input().split())
lis = list(map(int, input().split()))
lis.sort(reverse = True)

hap = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            tmp = (lis[i] + lis[j] + lis[k])
            if tmp >= hap and tmp <= m:
                hap = tmp

print(hap)