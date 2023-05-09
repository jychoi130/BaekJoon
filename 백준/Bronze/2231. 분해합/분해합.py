n = int(input())
val = 1
chk = True
while n >= val:
    hap = val
    for i in range(len(str(val))):
        hap += int(str(val)[len(str(val))-i-1])
    if hap == n:
        print(val)
        chk = False
        break
    val += 1
if chk: print('0')