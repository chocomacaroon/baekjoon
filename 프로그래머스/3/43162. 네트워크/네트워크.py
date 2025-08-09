def dfs(pos, n, computers, visited):
    for i in range(0, n):
        if not visited[i] and computers[pos][i] == 1:
            visited[i] = True
            dfs(i, n, computers, visited)
        
        
def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i, n, computers, visited)
    return answer