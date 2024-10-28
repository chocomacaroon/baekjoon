s = input()
answer = ""
for c in s:
    if c.isupper():
        answer += c.lower()
    else:
        answer += c.upper()
print(answer)