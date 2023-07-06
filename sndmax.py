n = int(input())
while n > 0:
    l = list(map(int,input().split()))
    l.remove(max(l))
    print(max(l))
    n -= 1
