t = int(input())
while t > 0:
    x,y = map(int,input().split())
    if x < y:
        print("PROFIT")
    elif x == y:
        print("NEUTRAL")
    else:
        print("LOSS")
    t -= 1 
