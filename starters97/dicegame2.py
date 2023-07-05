t = int(input())
while t > 0:
    a1,a2,a3,b1,b2,b3 = map(int,input().split())
    suma = a1+a2+a3 - min(a1,a2,a3)
    sumb = b1+b2+b3 - min(b1,b2,b3)
    if suma > sumb:
        print("Alice")
    elif suma < sumb:
        print("Bob")
    else:
        print("Tie")
    t -= 1    
