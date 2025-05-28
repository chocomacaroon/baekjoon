n = int(input())
rainbow = ["ChongChong"]
for i in range(n):
  A, B = input().split()
  if A in rainbow and B not in rainbow:
    rainbow.append(B)
  elif B in rainbow and A not in rainbow:
    rainbow.append(A)
print(len(rainbow))