numbers = ["","", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
words = input()
sum = 0
for i in words:
  for a in numbers:
    if i in a:
      sum += numbers.index(a)
print(sum+len(words))
