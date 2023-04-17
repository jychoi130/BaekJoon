import math

a = int(input())
b = list(map(int, input().split()))
count = 0

for i in b:
    chk = True
    s = math.sqrt(i)
    if s == math.floor(s): 
        continue
    for j in range(2, i):
        if i % j == 0: 
            chk = False
            break
    if chk:     
        count += 1
    
print(count)