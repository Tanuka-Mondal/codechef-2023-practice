a,b = map(int, input().split())
s = a+b 
m = a*b 
if s>m:
    print(s-m)
else:
    print(m-s)
