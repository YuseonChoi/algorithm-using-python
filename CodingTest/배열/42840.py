""" [모의고사] https://school.programmers.co.kr/learn/courses/30/lessons/42840 """

# solution 1
def solution(answers):
    target = []
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]

    scores = [0]*3
    # 수포자별 패턴과 정답이 얼마나 일치하는지 확인
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i%len(pattern)]:
                scores[j]+=1
    
    # 최고 점수 저장
    max_score = max(scores)
    
    # 최고 점수를 가진 수포자들을 찾아 리스트에 저장
    for s, score in enumerate(scores):
        if scores[s] == max_score:
            target.append(s+1)

    return target

# solution 2
def solution(answers):
    target = []
    scores = [0,0,0]
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]

    for i, answer in enumerate(answers):
        if answer == s1[i%len(s1)]:
            scores[0]+=1
        if answer == s2[i%len(s2)]:
            scores[1]+=1
        if answer == s3[i%len(s3)]:
            scores[2]+=1
        
    # 최고 점수 저장
    max_score = max(scores)
    
    # 최고 점수를 가진 수포자들을 찾아 리스트에 저장
    for s, score in enumerate(scores):
        if scores[s] == max_score:
            target.append(s+1)

    return target


"""
잘 안풀리길래 책 코드를 보고 solution1을 제출했다.
맨 처음에 생각한 풀이가 맞았는데 끝까지 시도해보지 못했던 게 아쉬웠다.
다음 번에는 좀 더 인내심을 가지고 문제를 풀도록 하자. 
"""