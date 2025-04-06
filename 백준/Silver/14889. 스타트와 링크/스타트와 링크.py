N = int(input())
team = []
for _ in range(N):
    team.append(list(map(int, input().split())))
###################################
case = []
stack = []
answer = []
###################################
def factorial(n):
    result = 1
    if n <= 1:
        return 1
    for i in range(1,n+1):
        result *= i
    return result

def nCr(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))
###################################
i = 0
ma = nCr(N,N//2)//2 #
# ma = 3 #
se = set([i for i in range(N)])

while len(case) < ma: #반만하기 중복 투머치임
    while i >= N:
        n = stack.pop()
        i = n + 1
    stack.append(i)
    if len(stack) == N//2:
        # case.append([stack[:])
        case.append([stack[:], list(se-set(stack))])
        n = stack.pop()
        i = n + 1
    else:
        i += 1
# print(*case,sep='\n')
###################################

#두개 조합 구하는 부분 구현

mi = 100000 #최대값설정

#정확한 요소로 설정하기
for A,B in case:
    A_score = 0
    B_score = 0
    for i in range(N//2-1):
        for j in range(i+1,N//2):
            A_score += team[A[i]][A[j]]
            A_score += team[A[j]][A[i]]
    for i in range(N//2-1):
        for j in range(i+1,N//2):
            B_score += team[B[i]][B[j]]
            B_score += team[B[j]][B[i]]
    # print(A_score, B_score)
    if abs(A_score-B_score) < mi:
        mi = abs(A_score-B_score)

print(mi)