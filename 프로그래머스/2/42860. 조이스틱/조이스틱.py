# def solution(name):
#     answer = 0
#     word = list("A"*len(name))
#     cursor = 0
#     for i in range(len(word)):
#         # print(min(ord(name[i])-ord("A"), ord("Z")-ord(name[i])+1))
#         answer+=(min(ord(name[i])-ord("A"), ord("Z")-ord(name[i])+1))
#     name2 = list(name)
#     #커서이동
#     name2[0] = "A"
#     while name2 != word:
#         #오른쪽이동, 왼쪽이동 더 가까운쪽으로 이동하기
#         for i in range(1,len(name)):
#             rpos = (cursor + i)%len(name)
#             lpos = (cursor - i)%len(name)
#             # print(i,rpos,lpos, name2[rpos], name2[lpos])
#             if name2[rpos]!="A":
#                 cursor = rpos
#                 answer += i
#                 name2[cursor] = "A"
#                 break
#             elif name2[lpos]!="A":
#                 cursor = lpos
#                 answer += i
#                 name2[cursor] = "A"
#                 break
#     return answer

def solution(name):
    answer = 0
    n = len(name)
    
    # 상하 조작 먼저 계산
    for i in range(n):
        answer += min(ord(name[i]) - ord("A"), ord("Z") - ord(name[i]) + 1)
    
    # 좌우 조작 최솟값 초기값은 그냥 오른쪽으로 쭉 가는 경우
    move = n - 1

    for i in range(n):
        next_idx = i + 1
        # 연속된 A가 끝나는 위치 찾기
        while next_idx < n and name[next_idx] == "A":
            next_idx += 1
        # 오른쪽으로 i칸 → 뒤로 돌아서 n - next_idx칸
        # 또는 반대로 먼저 뒤로 갔다가 앞으로 오는 경우 비교
        move = min(move, i + n - next_idx + min(i, n - next_idx))
    
    answer += move
    return answer

