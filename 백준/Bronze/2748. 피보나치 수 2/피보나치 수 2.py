num = [0, 1]
n = int(input())
if n < 2:
    print(num[n])
else:
  for i in range(2,n+1):
    num.append(num[i-1]+num[i-2])
  print(num[-1])