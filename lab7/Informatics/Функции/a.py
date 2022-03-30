def mini(a, b, c, d):
    print(min(min(a, b), min(c, d)))
a, b, c, d = input().split()
mini(a, b, c, d)