str = input()
answer = ''
for c in str:
    if c.islower():
        answer += c.upper()
    else:
        answer += c.lower()
print(answer)