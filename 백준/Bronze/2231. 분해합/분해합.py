n = int(input())
for m in range(1,n+1):
    nums = list(str(m))
    if sum(list(map(int,nums)))+m == n:
        print(m)
        break
else:
    print(0)