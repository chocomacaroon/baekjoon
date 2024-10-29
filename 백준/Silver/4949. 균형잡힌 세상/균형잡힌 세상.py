import sys

input = sys.stdin.readline

while True:
    s = input()
    if s == ".\n":
        break
    stack = []
    for c in s:
        if c == "(" or c == "[":
            stack.append(c)
        elif c == ")":
            if len(stack) and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(c)
        elif c == "]":
            if len(stack) and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(c)
    if len(stack):
        print("no")
    else:
        print("yes")