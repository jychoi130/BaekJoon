n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(input())
    
ans = []
for i in range(n - 7):
    for j in range(m - 7):
        count = 0
        for k in range(8):
            for l in range(8):
                if (k+l) % 2 == 0:
                    if data[k+i][l+j] == "B":
                        count += 1
                else: 
                    if data[k+i][l+j] == "W":
                        count += 1
        ans.append(count)
        ans.append(64-count)
print(min(ans))