while True:
    n = int(input())
    sum = 0
    if n == -1: break
    for i in range(1, n):
        if n % i == 0:
          sum += i
    if sum == n:
        print(n,'= ',end='')
        print(1,end='')
        for i in range(2,n):
            if n % i == 0:
              print(' +',i,end='')
        print()
    else:
       print(n, 'is NOT perfect.')