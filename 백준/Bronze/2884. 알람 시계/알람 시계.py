a, b = map(int, input().split())
if b < 45:
    if a == 0:
        a = 23
    else: a -= 1
    b = b + 15
else:
    b -= 45
print(a, b)