""" [소수 만들기] https://school.programmers.co.kr/learn/courses/30/lessons/12977?language=python3 """

import itertools

def solution(nums):
    sum_list = []
    num = 0
    # 3개의 값을 뽑음
    values = list(itertools.combinations(nums, 3))
    # 뽑은 3개의 값의 합을 구해 sum_list에 저장
    for v in range(len(values)):
        sum_list.append(sum(values[v]))
        
    # sum_list에 있는 값을 하나씩 불러와 소수인지 판별 (에라토스테네스의 체)
    for s in sum_list:
        flag = True
        if s < 2:
            flag = False
        for i in range(2, int(s**0.5)+1):
            if s%i==0:
                flag = False
        if flag:
            num+=1 
        
    return num
