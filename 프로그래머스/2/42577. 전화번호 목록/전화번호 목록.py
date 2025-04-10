def solution(phone_book):
    answer = True
    tmp = []
    phone_book.sort(key = lambda x:(x,len(x)))
    for i in range(1,len(phone_book)):
        if phone_book[i].startswith(phone_book[i-1]):
            return False
    return answer