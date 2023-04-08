a, b = input().split()
a = int(a[::-1])
b = int(b[::-1])
print('{0}'.format(a if a > b else b))
