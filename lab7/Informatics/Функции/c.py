def xor(x, y):
    return (int(x) ^ int(y))
x, y = input().split()
if xor(x, y):
    print(1)
else:
    print(0)