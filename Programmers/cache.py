""" <캐시> https://programmers.co.kr/learn/courses/30/lessons/17680 """

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)  # maxlen: deque의 길이의 최댓값을 설정

    for c in cities:
        c = c.lower()   # 대소문자 구분 X
        
        # cache hit - 캐시 내 데이터가 존재할 경우
        # 같은 데이터가 중복해서 들어갈 수 없으므로 remove 후 다시 append 작업
        if c in cache:
            cache.remove(c)
            cache.append(c)
            answer += 1
        # cache miss - 캐시 내 데이터가 존재하지 않을 경우
        else:
            cache.append(c)
            answer += 5
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))    # 50
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))           # 21