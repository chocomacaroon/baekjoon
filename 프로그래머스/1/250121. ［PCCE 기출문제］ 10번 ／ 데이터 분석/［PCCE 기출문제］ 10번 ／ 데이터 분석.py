def solution(data, ext, val_ext, sort_by):
    answer = []
    if sort_by == "code": i = 0
    elif sort_by == "date":i=1
    elif sort_by == "maximum":i=2
    elif sort_by == "remain":i=3
    
    if ext == "code": i2 = 0
    elif ext == "date":i2=1
    elif ext == "maximum":i2=2
    elif ext == "remain":i2=3
    sort = sorted(data,key=lambda x:x[i])
    for n in sort:
        a,b,c,d = n
        if i2==0:
            if a < val_ext:
                answer.append(n)
        if i2==1:
            if b < val_ext:
                answer.append(n)
        if i2==2:
            if c < val_ext:
                answer.append(n)
        if i2==3:
            if d < val_ext:
                answer.append(n)
    return answer