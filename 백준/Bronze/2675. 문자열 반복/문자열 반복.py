n = int(input())
for i in range(n):
    num, s = input().split()
    for j in s:
        for k in range(int(num)):
            print(j, end = '')
    print()