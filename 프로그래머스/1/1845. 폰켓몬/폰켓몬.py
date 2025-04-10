def solution(nums):
    answer = 0
    se = set(nums)
    if len(se) <= len(nums)//2:
        return len(se)
    else:
        return len(nums)//2
