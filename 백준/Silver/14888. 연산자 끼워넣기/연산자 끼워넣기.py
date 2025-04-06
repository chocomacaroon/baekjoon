N = int(input())
num_lst = list(map(int, input().split()))
op_cnt = list(map(int, input().split()))

mi = float('inf')
ma = -float('inf')

def calc(idx, result, plus,minus,mul,div):
    global mi, ma
    if idx == N:
        mi = min(mi, result)
        ma = max(ma, result)
        return

    if plus:
        calc(idx+1, result+num_lst[idx], plus-1, minus, mul, div)
    if minus:
        calc(idx+1, result-num_lst[idx], plus, minus-1, mul, div)
    if mul:
        calc(idx+1, result*num_lst[idx], plus, minus, mul-1, div)
    if div:
        if result < 0:
            calc(idx+1, -((-result)//num_lst[idx]), plus, minus, mul, div-1)
        else:
            calc(idx + 1, result//num_lst[idx], plus, minus, mul, div - 1)

calc(1, num_lst[0], op_cnt[0], op_cnt[1], op_cnt[2], op_cnt[3])

print(ma)
print(mi)