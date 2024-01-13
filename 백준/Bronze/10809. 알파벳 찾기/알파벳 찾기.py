S = input()
a = ord('a')
z = ord('z')
for i in range(a, z+1):
  print(S.find(chr(i)), end=' ')