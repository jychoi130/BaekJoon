lis = []
for i in range(10):
    lis.append(int(input()) % 42)
ans = set(lis)
print(len(ans))