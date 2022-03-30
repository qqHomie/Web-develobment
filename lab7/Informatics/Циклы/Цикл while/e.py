n = int(input())
p = 1
k = 0
while(1):
    if p >= n:
        print(k)
        break
    p *= 2
    k += 1