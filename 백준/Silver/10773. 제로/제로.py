k = int(input())
lis = []
for i in range(k):
    n = int(input())
    if n == 0:
        try:
            lis.pop()
        except: pass
    else:
        lis.append(n)
print(sum(lis))