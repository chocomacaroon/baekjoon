import sys
input = sys.stdin.readline

N,M = map(int,input().strip().split())
store = {}
for _ in range(N):
    address,pw = input().strip().split()
    store[address]=pw
for _ in range(M):
    c = input().strip()
    print(store[c])