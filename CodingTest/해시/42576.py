""" [완주하지 못한 선수] https://school.programmers.co.kr/learn/courses/30/lessons/42576 """

# solution 1
def solution(participant, completion):
    dic = {}
    for p in participant:
        # dic[p] = participant.count(p)  # 시간 초과남
        if p in dic.keys():
            dic[p]+=1
        else:
            dic[p]=1
            
    
    for c in completion:
        dic[c] -=1
        
    for key in dic.keys():
        if dic[key] > 0:
            return key


# solution 2
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]