s = input()
a = 4.3

if s == "F":
    s += "+"
if s[0] == 'B': 
    a -= 1
elif s[0] == 'C':
    a -= 2
elif s[0] == 'D':
    a -= 3
elif s[0] == 'F':
    a = 0.0
    
if s[1] == '0': 
    a -= 0.3
elif s[1] == '-':
    a -= 0.6

print(round(a, 1))