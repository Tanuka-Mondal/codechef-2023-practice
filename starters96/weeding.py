t = int(input ())
while t > 0:
    n,m,k = map(int,input().split())
    a = list(map(int, input ().split()))
    if (m-a[-1]+1) >= k:
        print("yes")
    else:
        print("no")
    t -= 1
