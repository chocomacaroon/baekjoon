s = input()
string = []
for i in range(len(s)):
    string.append(s[-i:])
print(*sorted(string),sep = "\n")