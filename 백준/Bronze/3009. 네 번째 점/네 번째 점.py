x = set()
y = set()
for i in range(3):
  A, B = map(int, input().split())
  if A in x:
    x.remove(A)
  else:
    x.add(A)
  if B in y:
    y.remove(B)
  else:
    y.add(B)
print(*x, *y)