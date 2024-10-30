import sys

input = sys.stdin.readline

N = int(input().strip())
stack = []
num = 1
opt = []
find = True
for _ in range(N):
  c = int(input().strip())
  if num <= c:
    while num <= c:
      stack.append(num)
      opt.append("+")
      num+=1
  if stack[-1] == c:
    stack.pop(-1)
    opt.append("-")
  else:
    find = False

if not find:
  print("NO")
else:
  print(*opt,sep="\n")

#불가능한 경우