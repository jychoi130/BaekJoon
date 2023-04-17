words = set()
for i in range(int(input())):
    words.add(input())
ans = sorted(words, key = (lambda x : (len(x), x)))
for i in ans:
    print(i)