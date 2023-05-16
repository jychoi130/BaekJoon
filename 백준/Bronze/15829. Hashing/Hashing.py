L = int(input())
s = input()

ans = 0
count = 0

for i in s:
    chk = 1
    for j in range(count):
        chk *= 31
    ans += ((ord(i)-96)*chk)
    count += 1

print(ans)