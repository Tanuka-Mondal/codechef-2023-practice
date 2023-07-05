q = int(input())

while q > 0:
    n = int(input())
    s = input()
    t = input()
    u = input()
    st = "abcdefghijklmnopqrstuvwxyz"
    dif = (ord(t[0]) - ord(s[0])) % 26
    ne = ""
    
    for i in range(n):
        idx = (st.index(u[i]) + dif) % 26
        ne += st[idx]
    
    print(ne)
    q -= 1
