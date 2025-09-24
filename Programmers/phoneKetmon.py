""" <폰켓몬> https://school.programmers.co.kr/learn/courses/30/lessons/1845 """

def solution(nums):

    n1 = len(nums)
    n2 = len(set(nums))
    
    if n1//2 < n2:
        return n1//2
    else:
        return n2