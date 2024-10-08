def solution(survey, choices):
    answer = ''
    mbti = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    for s,ans in zip(survey,choices):
        a,b = list(s)
        if ans==7:
            mbti[b]+=3
        elif ans==6:
            mbti[b]+=2
        elif ans==5:
            mbti[b]+=1
        elif ans==4:
            pass
        elif ans==3:
            mbti[a]+=1
        elif ans==2:
            mbti[a]+=2
        elif ans==1:
            mbti[a]+=3
    if mbti["R"] >= mbti["T"]:
        answer+="R"
    else:
        answer+="T"
    if mbti["C"] >= mbti["F"]:
        answer+="C"
    else:
        answer+="F"
    if mbti["J"] >= mbti["M"]:
        answer+="J"
    else:
        answer+="M"
    if mbti["A"] >= mbti["N"]:
        answer+="A"
    else:
        answer+="N"
    return answer