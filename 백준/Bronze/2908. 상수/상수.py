num1, num2 = input().split()
num1_rev = num1[::-1]
num2_rev = num2[::-1]
if num1_rev > num2_rev:
  print(num1_rev)
else:
  print(num2_rev)