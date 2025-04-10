def solution(numbers, target):
    answer = 0
    return dfs(0,0,numbers, target)

def dfs(i, result, numbers, target):
    if i == len(numbers):
        if result == target:
            print(result)
            return 1
        return 0
    return dfs(i+1, result+numbers[i], numbers, target) + dfs(i+1, result-numbers[i], numbers, target)