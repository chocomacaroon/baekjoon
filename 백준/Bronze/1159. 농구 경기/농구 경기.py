N = int(input())
names = dict()
for i in range(N):
    s = input()
    if s[0] in names.keys():
        names[s[0]] += 1
    else:
        names[s[0]] = 1

answer = []

for k in names:
    if names[k] >= 5:
        answer.append(k)

if len(answer) == 0:
    print("PREDAJA")
else:
    print(*sorted(answer), sep='')