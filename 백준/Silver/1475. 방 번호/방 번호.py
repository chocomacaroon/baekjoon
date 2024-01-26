N = input()
numbers = [0 for i in range(9)]
for i in N:
  if i == '9':
    numbers[6] += 1
  else:
    numbers[int(i)] += 1
numbers[6] = numbers[6] // 2 + numbers[6] % 2
print(max(numbers))