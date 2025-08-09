answer = 0

def dfs(su, pos, numbers, target):
    global answer
    if pos == len(numbers):
        if su == target:
            answer += 1
        return
    dfs(su + numbers[pos], pos+1, numbers, target)
    dfs(su - numbers[pos], pos+1, numbers, target)

def solution(numbers, target):
    dfs(0, 0, numbers, target)
    return answer