def dfs(depth, numbers, target, su):
    if depth == len(numbers):
        if su == target:
            return 1
        else:
            return 0
    return dfs(depth+1, numbers, target, su + numbers[depth]) + dfs(depth+1, numbers, target, su - numbers[depth])
    

def solution(numbers, target):
    return dfs(0, numbers, target, 0)