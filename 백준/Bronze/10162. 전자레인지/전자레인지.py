n = int(input())
a = n//300
n %= 300
b = n//60
n %= 60
if n%10 == 0:
    c = n//10
    print(a,b,c)
else:
    print(-1)