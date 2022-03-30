from math import sqrt

n = int(input())
x = 1
while(x <= n):
    if x == int(sqrt(x)) * int(sqrt(x)):
        print(x)
    x += 1