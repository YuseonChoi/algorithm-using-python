""" [구명보트] https://school.programmers.co.kr/learn/courses/30/lessons/42885 """

def solution(people, limit):
    count = 0  # 필요한 구명보트 개수
    # 가장 무거운 사람과 가장 가벼운 사람을 짝을 지음
    people.sort()
    
    i = 0  # 가장 가벼운 사람을 가르키는 인덱스
    j = len(people)-1  # 가장 무거운 사람을 가르키는 인덱스
    
    while i<=j:
        if people[i] + people[j] <= limit:
            i+=1
        j-= 1
        count += 1
        
    return count