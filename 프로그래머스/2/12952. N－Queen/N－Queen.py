def dfs(column, rows, diag1, diag2, n):
    if column == n:
        return 1
    count = 0
    for row in range(n):
        if (row not in rows) and ((column-row) not in diag1) and (column+row not in diag2):
            count += dfs(column+1, rows + [row], diag1 + [(column-row)], diag2 + [column+row], n)
    return count
        
def solution(n):
    rows = []
    diag1 = []
    diag2 = []
    return dfs(0, rows, diag1, diag2, n)