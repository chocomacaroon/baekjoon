n = int(input())
s = input()
answer = ""
for _ in range(n-1):
    s2 = input()
    answer = ""
    for c1,c2 in zip(s,s2):
        if c1 != c2:
            answer += "?"
        else:
            answer += c1
    s = answer
if n==1:
    print(s)
else:
    print(answer)