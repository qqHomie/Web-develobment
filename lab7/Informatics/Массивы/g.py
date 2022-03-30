n = int(input())
a = [int(i) for i in input().split()]
for i in range(n, 0, -1):
    print(a[i-1], end=" ")