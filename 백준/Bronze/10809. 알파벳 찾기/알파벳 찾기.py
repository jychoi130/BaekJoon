s = input()
ans = []
for i in range(ord('a'), ord('z') + 1):
    ans.append(s.find(chr(i)))
for i in ans:
    print(i, end = ' ')