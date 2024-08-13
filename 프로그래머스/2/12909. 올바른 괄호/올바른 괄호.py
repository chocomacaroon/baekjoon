def solution(s):
    stack = []
    for ch in s:
        if ch == '(' : stack.append(ch)
        else:
            if stack: stack.pop()
            else: return False
    return not stack
    
    
import sys
s = sys.stdin.readline()
print(solution(s))
#     answer = True
    
#     # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
#     print('Hello Python')

#     return True