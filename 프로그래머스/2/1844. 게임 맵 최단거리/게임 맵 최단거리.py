def solution(maps):
    result = bfs(maps)
    return result if result > 0 else -1

def bfs(maps):
    n, m = len(maps), len(maps[0])
    queue = [(0, 0, 1)]  # (x, y, 거리)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 하, 상, 우, 좌
    
    while queue:
        x, y, distance = queue.pop(0)  # 큐의 앞에서 요소 제거
        
        # 목적지에 도착한 경우
        if x == n - 1 and y == m - 1:
            return distance
        
        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            
            # 유효한 좌표 및 방문 가능 여부 체크
            if 0 <= next_x < n and 0 <= next_y < m and maps[next_x][next_y] == 1:
                maps[next_x][next_y] = 0  # 방문 처리
                queue.append((next_x, next_y, distance + 1))  # 큐에 추가

    return -1  # 목적지에 도달할 수 없는 경우
