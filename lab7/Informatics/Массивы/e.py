n = int(input())
a = [int(i) for i in input().split()]
flag = True
for i in range(1, n):
    if (a[i] > 0 and a[i - 1] > 0) or (a[i] < 0 and a[i - 1] < 0):
        print("YES")
        flag = False
        break
if flag:
    print("NO")