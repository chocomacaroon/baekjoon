while True:
  s = int(input())
  s = str(s)
  if s == '0':
    break
  if s == s[::-1]:
    print('yes')
  else:
    print('no')