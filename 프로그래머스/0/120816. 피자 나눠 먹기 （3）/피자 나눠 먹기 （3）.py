def solution(slice, n):
    return n//slice + int(bool(n%slice))