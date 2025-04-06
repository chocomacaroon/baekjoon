from collections import deque
T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    visited = [False for _ in range(N)]
    answer = 0

    for i in range(N):
        if not visited[i]:
            answer += 1
            cur = i
            while not visited[cur]:
                visited[cur]=True
                cur = arr[cur]-1
    print(answer)