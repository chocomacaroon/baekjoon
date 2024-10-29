N = int(input())
present = set()
for _ in range(N):
    name, com = input().split()
    if com == "enter":
        present.add(name)
    elif com == "leave":
        present.discard(name)


for n in sorted(present, reverse=True):
    print(n)