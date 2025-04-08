N, M = map(int, input().split())
r, c, d = map(int, input().split())
#움직이는 방향 : 위 오른 아래 왼
dir_x = [-1,0,1,0]
dir_y = [0,1,0,-1]
direction = ['위', '오른','아래','왼']
#왼쪽 90도 회전 dir회전 순서 인덱스
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
# print(*graph, sep='\n')
cnt = 0
####################################################
def robot(r,c,d):
    # print(f'현재위치 {r,c} 방향 {direction[d]}')
    global cnt
    if graph[r][c] == 0:
        cnt += 1
        # print("현재칸 청소")
        graph[r][c] = 2
    idx = (d - 1) % 4
    for i in range(4):
        # print(f'회전 {i+1}번')
        dirx = dir_x[idx]
        diry = dir_y[idx]
        nx = r + dirx
        ny = c + diry
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
            # print(f'{i+1}번 회전후 {direction[idx]}전진해서 함수 재귀')
            robot(nx,ny,idx)
            return
        idx = (idx - 1) % 4
    if 0 <= r+dir_x[(d-2)%4] < N and 0 <= c+dir_y[(d-2)%4] < M and graph[r+dir_x[(d-2)%4]][c+dir_y[(d-2)%4]] != 1:
        # print("후진")
        # print(f'정방향 {direction[d]} 후진방향 {direction[(d-2)%4]}')
        robot(r+dir_x[(d-2)%4], c+dir_y[(d-2)%4], d)
    # 후진 안되면 종료
    # else:
        # print("종료")
    return

robot(r, c, d)
print(cnt)