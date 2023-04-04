n = int(input())
lis = list(map(int, input().split()))
v = int(input())
count = 0
for i in range(len(lis)):
    if lis[i] == v:
        count += 1
print(count)