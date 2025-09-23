""" <H-Index> https://school.programmers.co.kr/learn/courses/30/lessons/42747 """

def solution(citations):
    h = 0
    citations.sort(reverse=True)
    
    for i, c in enumerate(citations, start=1):
        if c >= i:
            h = i
        else:
            break
    return h
    
