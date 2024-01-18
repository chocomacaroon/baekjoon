min_ham = float('inf')
min_drink = float('inf')
for i in range(3):
  min_ham = min(int(input()), min_ham)
for _ in range(2):
  min_drink = min(int(input()), min_drink)
print(min_ham+min_drink-50)