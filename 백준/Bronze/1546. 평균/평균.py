n = int(input())
lis = list(map(int, input().split()))
m = max(lis)
hap = 0 
for i in lis:
    hap += round((i / m * 100), 2)
print(hap/n)