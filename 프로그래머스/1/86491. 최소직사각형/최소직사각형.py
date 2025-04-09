def solution(sizes):
    answer = 0
    mw = sizes[0][0]
    mh = sizes[0][1]
    for w,h in sizes[1:]:
        if max(mw,w)*max(mh,h) < max(mw,h)*max(mh,w):
            mw = max(mw,w)
            mh = max(mh,h)
        else:
            mw = max(mw,h)
            mh = max(mh,w)
        print(mw,mh)
    return mw*mh

#3 10
#8 5

#그냥 있을때
#돌릴때