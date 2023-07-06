t = int(input())
while t > 0:
    n,x = map(int,input().split())
    if n <= x:
        print("Yes")
    else:
        print("No")
    t -= 1   
