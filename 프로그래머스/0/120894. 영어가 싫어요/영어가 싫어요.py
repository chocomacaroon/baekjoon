def solution(numbers):
    answer = 0
    ans = ''
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    n = ''
    for c in numbers:
        n += c
        if n in nums:
            ans += str(nums.index(n))
            n = ''
        else:
            pass
    answer = int(ans)
    return answer