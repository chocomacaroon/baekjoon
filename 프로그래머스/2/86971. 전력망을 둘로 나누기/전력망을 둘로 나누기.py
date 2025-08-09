# from collections import deque

# def solution(n, wires):
#     answer = -1
#     ans = []
#     dic = {}
#     for i in range(len(wires)): 끊는 부분
#         for x,y in wires:
#             if x not in dic.keys():
#                 dic[x] = [y]
#             else:
#                 dic[x].append(y)
#             if y not in dic.keys():
#                 dic[y] = [x]
#             else:
#                 dic[y].append(x)

#         print(dic)
    
#     ###############
#         q = deque([1])
#         cnt1 = 0
#         v = [False]*(n+1)
#         v[1] = True

#         while q:
#             cnt1 += 1
#             k = q.pop()
#             if k in dic.keys():
#                 for l in dic[k]:
#                     if v[l] == False:
#                         v[l] = True
#                         q.append(l)

#         #############33
#         cnt2 = 0
#         for i in range(1, n+1):
#             if not v[i]:
#                 q = deque([i])
#             while q:
#                 k = q.pop()
#                 cnt2 += 1
#                 if k in dic.keys():
#                     for l in dic[k]:
#                         if v[l] == False:
#                             v[l] = True
#                             q.append(l)
#         ans.append(abs(cnt2-cnt1))
#     return min(ans)


from collections import deque

def bfs(start, dic, n):
    visited = [False] * (n+1)
    visited[start] = True
    q = deque([start])
    count = 1
    while q:
        k = q.popleft()
        for l in dic.get(k, []):
            if not visited[l]:
                visited[l] = True
                q.append(l)
                count += 1
    return count

def solution(n, wires):
    ans = []
    for i in range(len(wires)):
        # i번째 전선을 제외한 dic 만들기
        dic = {}
        for j, (x, y) in enumerate(wires):
            if j == i:
                continue
            dic.setdefault(x, []).append(y)
            dic.setdefault(y, []).append(x)
        
        # 첫 번째 네트워크 크기
        cnt1 = bfs(wires[i][0], dic, n)
        cnt2 = n - cnt1
        ans.append(abs(cnt1 - cnt2))
    return min(ans)
