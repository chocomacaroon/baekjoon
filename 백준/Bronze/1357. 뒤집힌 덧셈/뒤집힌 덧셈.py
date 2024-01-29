def rev(x):
    s = str(x)
    return int(s[::-1])

X, Y = map(int, input().split())
print(rev(rev(X)+rev(Y)))