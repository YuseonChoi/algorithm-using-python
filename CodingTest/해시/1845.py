""" [폰켓몬] https://school.programmers.co.kr/learn/courses/30/lessons/1845 """

# solution 1
def solution(nums):
    limit = len(nums)//2
    answer = len(list(set(nums)))
    
    if answer >= limit:
        return limit
    else:
        return answer
    
    
# solution 2
def solution(nums):
    return min(len(nums)/2, len(set(nums)))