a = ""
while(a != "."):
    a = input()
    if a == ".": break
    chk = True
    s = []
    for i in a:
        if i == ")":
            try:
                x = s.pop()
            except:
                x = ""
            if x != "(":
                print("no")
                chk = False
                break
        elif i == "]":
            try:
                x = s.pop()
            except:
                x = ""
            if x != "[":
                print("no")
                chk = False
                break
        elif i == "(" or i =="[":
            s.append(i)
    if chk:
        if len(s) == 0: print("yes")
        else: print("no")