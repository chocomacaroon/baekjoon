N = int(input())

answer = 0
visited_y = [False] * N
diag1 = [False] * N*2
diag2 = [False] * N*2

def nq(x):
    global answer
    if x == N: #종료 조건
        answer+=1
        return
    for y in range(N):
        if not visited_y[y] and not diag1[x-y + (N-1)] and not diag2[x+y]:
            visited_y[y] = True
            diag1[x-y + (N-1)] = True
            diag2[x+y] = True
            nq(x+1)
            visited_y[y] = False
            diag1[x - y + (N-1)] = False
            diag2[x + y] = False
    return

nq(0)
print(answer)