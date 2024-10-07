# def solution(people, limit):
#     answer = 0
#     people = sorted(people,reverse=True)
#     i=0
#     j=len(people)-1
#     while True:
#         if people[i]+people[j] <= limit:
#             i+=1
#             j-=1
#             answer+=1
#         else:
#             if j-i==1:
#                 return answer+2
#             answer+=1
#             i+=1
#         if i >= j:
#             return answer
#     return answer

def solution(people, limit):
    answer = 0
    people = sorted(people, reverse=True)
    i = 0
    j = len(people) - 1

    while i <= j:
        # 가장 무거운 사람과 가장 가벼운 사람의 합이 limit 이하일 때
        if people[i] + people[j] <= limit:
            j -= 1  # 가장 가벼운 사람도 태움
        # 가장 무거운 사람만 태울 경우
        i += 1
        answer += 1

    return answer
