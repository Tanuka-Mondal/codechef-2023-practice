t = int(input())
while t > 0:
    x,y = map(int,input().split())
    if 2*x > 5*y:
        print("chocolate")
    elif 2*x < 5*y:    
        print("candy")
    else:
        print("either")
    t -= 1   
