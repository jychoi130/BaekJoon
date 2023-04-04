a = int(input())
for i in range(a):
    n, s = input().split()
    for j in s:
        for k in range(int(n)):
            print(j, end = '')
    print()