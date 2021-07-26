''' <모의고사>

https://programmers.co.kr/learn/courses/30/lessons/42840

'''

''' solution-1 딕셔너리 이용 '''

s1 = [1,2,3,4,5]
s1.extend(s1*2000)

s2 = [2,1,2,3,2,4,2,5]
s2.extend(s2*1250)

s3 = [3,3,1,1,2,2,4,4,5,5]
s3.extend(s3*1000)

dic = {1:0, 2:0, 3:0}

def solution(answers):
    answer = []
    for i in range(len(answers)):
        if s1[i] == answers[i]:
            dic[1] += 1
        if s2[i] == answers[i]:
            dic[2] += 1
        if s3[i] == answers[i]:
            dic[3] += 1
    
    res = max(dic.values())
    for key, value in dic.items():
        if res == value:
            answer.append(key)
        
    return answer



''' solution-2 enumerate 이용 '''

def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result