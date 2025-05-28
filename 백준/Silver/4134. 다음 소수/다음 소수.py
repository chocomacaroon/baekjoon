def isPrime(n):
  if n <= 1:
    return False
  for i in range(2 ,int(n**0.5)+1):
    if n % i == 0:
      return False
  return True

n = int(input())
for _ in range(n):
  num = int(input())
  while True:
    if isPrime(num):
      print(num)
      break
    num += 1