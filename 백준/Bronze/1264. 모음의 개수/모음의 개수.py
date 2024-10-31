moem = ["a","e","i","o","u"]

while True:
    s = input()
    if s == "#":
        break
    cnt = 0
    for c in s:
        if c.lower() in moem:
            cnt+=1
    print(cnt)