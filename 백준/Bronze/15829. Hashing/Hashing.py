n = int(input())
s = list(input())
answer = 0
for i,c in enumerate(s):
    answer += (31**i)*(ord(c)-ord('a')+1)
print(answer)