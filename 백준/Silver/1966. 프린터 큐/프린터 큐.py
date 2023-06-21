n = int(input())
for i in range(n):
    num, target = map(int, input().split())
    
    a = list(map(int, input().split()))
    b = list(range(num)) 
    
    count = 0
    while target in b:
        temp = a.pop(0)
        btemp = b.pop(0)
        try:
            if max(a) > temp:
                a.append(temp)
                b.append(btemp)
                continue
            else: count += 1
        except: count += 1
    print(count)