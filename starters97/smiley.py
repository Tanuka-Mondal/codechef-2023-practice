t = int(input())
while t > 0:
    n = int(input())
    s = input()
    smle = ""
    c = 0
    for i in range(n):
        if s[i] == ':':
            if smle == "":
                smle += s[i]
            elif smle == ':':
                smle = ":"
            else:
                smle = ":"
                c += 1
        elif s[i] == '(':
            smle = ""
        elif s[i] == ')':
            if smle != "":
                smle += s[i]
    print(c)  
    t -= 1
