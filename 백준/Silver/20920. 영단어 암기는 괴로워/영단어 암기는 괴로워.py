
import sys

N, M = map(int, sys.stdin.readline().split())
book = dict()
for i in range(N):
    s = sys.stdin.readline().strip()
    if len(s) >= M:
        if s not in book:
            book[s] = 1
        else:
            book[s] += 1

#1. 자주 나오는 단어, 2. 단어 길이, 3. 알파벳 사전 순
sorted_lst = sorted(book, key = lambda x:(-book[x],-len(x),x))

print(*sorted_lst,sep='\n')