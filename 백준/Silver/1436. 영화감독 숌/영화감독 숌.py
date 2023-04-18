n = int(input())
count = 0
a = 665
while True:
    a += 1
    if str(a).find('666') != -1 : 
        count+=1
    if count == n:
        break
print(a)