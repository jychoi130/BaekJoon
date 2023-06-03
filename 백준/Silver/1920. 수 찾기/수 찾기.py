n = int(input())
nlis = set(map(int, input().split()))
m = int(input())
mlis = list(map(int, input().split()))
for i in mlis:
    a = len(nlis)
    nlis.add(i)
    if len(nlis) != a:
        print("0")
    else: print("1")