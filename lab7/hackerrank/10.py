if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]
    maxi = max(arr)
    ans = []
    for i in arr:
        if i != maxi:
            ans.append(i)
    print(max(ans))
    