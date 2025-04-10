def solution(numbers):
    answer = 0
    lst = set()
    tmp = ""
    v = [0]*len(numbers)
    dfs(0,numbers,lst,tmp,v)
    print(*lst)
    for n in lst:
        if is_prime(n):
            answer+=1
    return answer

def dfs(n,numbers,lst, tmp, v):
    if n > 0:
        lst.add(int(tmp))
    if n==len(numbers):
        return
    for i in range(len(numbers)):
        if v[i] == 0:
            v[i] = 1
            dfs(n+1, numbers,lst,tmp+numbers[i],v)
            v[i] = 0

def is_prime(m):
    n = int(m)
    if n <= 1:
        return False
    if n <= 2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True
        