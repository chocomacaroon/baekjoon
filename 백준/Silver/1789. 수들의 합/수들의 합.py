N = int(input())
sum = 0
i = 1
nums = []
while True:
    sum += i
    nums.append(i)
    if sum > N:
        print(i-1)
        break
    i += 1