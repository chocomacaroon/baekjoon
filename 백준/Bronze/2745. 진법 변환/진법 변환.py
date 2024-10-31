s, n = input().split()
n = int(n)
answer = 0
s = s[::-1]
for i,c in enumerate(s):
    if c.isalpha():
        answer += (ord(c)-55)*(n**i)
    else:
        answer += int(c)*(n**i)
print(answer)