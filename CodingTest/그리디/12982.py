""" [예산] https://school.programmers.co.kr/learn/courses/30/lessons/12982 """

# solution 1 - 시간 초과 ㅠㅠ
from itertools import combinations

def solution(d, budget):
    answer = 1
    
    while True:
        sum_nums = []
        flag = []
        comb_nums = list(combinations(d,answer))
        for i in comb_nums:
            sum_nums.append(sum(i))


        for j in sum_nums:
            if j <= budget:
                flag.append(True)
            else:
                flag.append(False)
            
        if sum(flag)==0:
            return answer-1 
            
        answer += 1
        
        
# solution 2 - 정답
def solution(d, budget):
    d.sort()
    answer = 0
    for amount in d:
        if amount > budget:
            break
        else:
            budget -= amount
            answer += 1
    
    return answer

"""
문제를 더 쉽게 풀 수 있는 방법을 모색해야 한다.
복잡하게 생각하지 말자.
"""