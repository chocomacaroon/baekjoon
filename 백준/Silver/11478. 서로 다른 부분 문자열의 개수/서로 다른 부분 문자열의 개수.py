s = list(input())
se = set()
for i in range(1,len(s)+1):
    for j in range(len(s)-i+1):
        se.add("".join(s[j:j+i]))
print(len(se))