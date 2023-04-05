lis = list(map(int, input().split()))
ans = 0
for i in lis:
    ans += (i**2)
print(ans%10)