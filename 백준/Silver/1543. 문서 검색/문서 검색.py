s = input()
find = input()
s2 = s.replace(find,"")
print((len(s)-len(s2))//len(find))