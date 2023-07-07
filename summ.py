t = int(input())
for z in range(t):
    a,b,c = map(int,input().split())
    if a+b == c:
        print("yes")
    else:
        print("no")
