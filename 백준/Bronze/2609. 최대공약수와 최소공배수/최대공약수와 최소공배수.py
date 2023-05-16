a, b = map(int, input().split())
gcd = 1

if a < b: chk = a
else: chk = b

for i in range(2, chk+1):
    if a % i == 0 and b % i == 0:
        gcd = i
    
print(gcd)
print(a*b//gcd)