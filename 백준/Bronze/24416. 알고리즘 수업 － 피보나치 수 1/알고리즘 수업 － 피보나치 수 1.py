N = int(input())
stack = [N]
cnt=0
while True:
    n = stack.pop(-1)
    if n > 2:
        stack.append(n-1)
        stack.append(n-2)
    elif n == 1 or n == 2:
        cnt+=1
    if len(stack) == 0:
        break
print(cnt, N-2)