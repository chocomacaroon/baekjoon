N = int(input())
result = N
num = []
for i in range(2, N+12
):
    while True:
      if result % i == 0:
        print(i)
        result //= i
      else:
         break