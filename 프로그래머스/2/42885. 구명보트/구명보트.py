from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    stk = deque(people)
    while stk:
        if len(stk) >= 2 and (stk[0]+stk[-1] <= limit):
            answer+=1
            stk.popleft()
            stk.pop()
        else:
            stk.popleft()
            answer+=1
    return answer

#80 70 50 50