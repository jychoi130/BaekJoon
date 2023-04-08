s = input().upper()
ans = {}
for i in s:
    count = 1
    if i in ans:
        count = ans[i] + 1
    ans[i] = count

count = 0
most = ""
chk = False

for i in ans:
    if ans[i] > count:
        count = ans[i]
        most = i
        chk = False
    elif ans[i] == count:
        chk = True

if chk: print('?')
else: print(most)