from math import sqrt


x = int(input())
cnt = 0
for i in range(1, sqrt(x)):
    if x%i == 0:
        cnt += 1
cnt *= 2
if sqrt(x) == int(sqrt(x)):
    cnt += 1
print(cnt)