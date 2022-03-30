def power(a, n):
    res = 1
    if n == 0:
        print(res)
        return
    else:
        for i in range(n):
            res *= a
    print(res)
a, n = input().split()
power(float(a), int(n))