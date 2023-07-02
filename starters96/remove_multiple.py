t = int(input())
while t > 0:
    n, m = map(int, input().split())
    q = set(map(int, input().split()))
    total_sum = (n * (n + 1)) // 2  
    q_sum = sum(q)
    result = total_sum - q_sum

    print(result)
    t -= 1
