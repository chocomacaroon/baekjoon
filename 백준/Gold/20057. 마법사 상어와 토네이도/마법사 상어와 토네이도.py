N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# print(graph)
dv = [[0, -1], [1, 0], [0, 1], [-1, 0]]

distance = 2
dv_i = 0
x, y = N//2, N//2
answer = 0

pro = [1, 2, 5, 7]

while True:
    dx, dy = dv[dv_i]
    if x+dx < 0 or y+dy < 0 or x+dx > N or y+dy > N:
        break
    for _ in range(distance//2):
        # print([x, y])
        x, y = x + dx, y + dy
        if x < 0 or y < 0 or x > N or y > N:
            break

        dust = graph[x][y]
        dust_div = {1: dust*1//100, 2: dust*2//100, 5: dust*5//100, 7: dust*7//100, 10: dust*10//100} #먼지 분산된 것들의 값
        #나머지
        dust_div[0] = dust - (2*dust_div[1] + 2*dust_div[2] + dust_div[5] + 2*dust_div[7] + 2*dust_div[10])
        move = dict()
        # print(dv_i)
        if dv_i == 0:
            move = {0: [(0, -1)], 1: [(1, 1), (-1, 1)], 2: [(-2, 0), (2, 0)], 5: [(0, -2)], 7: [(-1, 0), (1, 0)], 10: [(1, -1), (-1, -1)]}
        elif dv_i == 1:
            move = {0: [(1, 0)], 1: [(-1, -1), (-1, 1)], 2: [(0, 2), (0, -2)], 5: [(2, 0)], 7: [(0, -1), (0, 1)], 10: [(1, -1), (1, 1)]}
        elif dv_i == 2:
            move = {0: [(0, 1)], 1: [(-1, -1), (1, -1)], 2: [(-2, 0), (2, 0)], 5: [(0, 2)], 7: [(-1, 0), (1, 0)], 10: [(-1, 1), (1, 1)]}
        elif dv_i == 3:
            move = {0: [(-1, 0)], 1: [(1, -1), (1, 1)], 2: [(0, 2), (0, -2)], 5: [(-2, 0)], 7: [(0, -1), (0, 1)], 10: [(-1, -1), (-1, 1)]}
        else:
            print("Error")

        for k in move.keys():
            for dx2, dy2 in move[k]:
                nx, ny = x + dx2, y + dy2
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += dust_div[k]
                else:
                    answer += dust_div[k]
        graph[x][y] = 0
        # print(dv_i,[x,y])
        # print(*graph, sep='\n')
        # print(f'answer:{answer}')
    dv_i = (dv_i+1) % 4
    distance += 1
print(answer)