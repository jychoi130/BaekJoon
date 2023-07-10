T = int(input())
ans_lis = [[0]*15 for i in range(15)]

for i in range(15):
    ans_lis[0][i] = i + 1
for i in range(15):
    ans_lis[i][0] = 1

for i in range(1, 15):
    for j in range(1, 15):
        ans_lis[i][j] = (ans_lis[i-1][j] + ans_lis[i][j-1])

for i in range(T):
    k = int(input())
    n = int(input())
    print(ans_lis[k][n-1])