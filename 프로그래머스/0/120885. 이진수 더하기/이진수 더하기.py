def solution(bin1, bin2):
    print(int(bin1,2), int(bin2,2))
    return bin(int(bin1,2)+int(bin2,2))[2:]