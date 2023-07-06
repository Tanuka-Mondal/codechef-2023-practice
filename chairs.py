t = int(input())
while t > 0:
    x,y = map(int,input().split())
    if x > y:
        print(x-y)
    else:
        print(0)
    t -= 1  
