n = int(input())
while(1):
    if n == 1:
        print("YES")
        break
    elif n%2 == 1:
        print("NO")
        break
    n /= 2