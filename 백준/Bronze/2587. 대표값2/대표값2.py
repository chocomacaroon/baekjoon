nums = []
for i in range(5):
    nums.append(int(input()))
print(sum(nums)//len(nums))
nums_sort = sorted(nums)
print(nums_sort[2])