t = int(input ()) 
while t > 0 :
    n,x,k,p = map(int,input().split())
    sum = p
    if k > x:
        sum += (x*10) + (k-x)*5
        if n == k:
            sum += 20
    else :
        sum += k*10
        if n == k:
            sum += 20
    print(sum)
    t -= 1 
