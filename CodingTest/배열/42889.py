""" [배열] https://school.programmers.co.kr/learn/courses/30/lessons/42889 """

def solution(N, stages):
    total = len(stages)
    
    # 0 [1~N] N+1
    challengers = [0] * (N+2)
    
    failrate = {}
    
    for s in stages:
        challengers[s]+=1
    
    for i in range(1,N+1):
        if challengers[i] == 0:
            failrate[i] = 0
        else:
            failrate[i] = challengers[i] / total
            total -= challengers[i]
    
    # 실패율이 높은 것부터 내림차순으로 정렬
    # sorted(dic, key=lambda ~) -> 특정 기준으로 정렬된 정렬된 딕셔너리 키값 반환
    result = sorted(failrate, key=lambda x : failrate[x], reverse=True)
        
    return result 