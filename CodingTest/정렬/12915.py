""" [문자열 내 마음대로 정렬하기] https://school.programmers.co.kr/learn/courses/30/lessons/12915 """

# solution 1
import heapq

def solution(strings, n):
    str_list = []
    answer = []
    
    for str in strings:
        str_list.append((str[n], str))
        heapq.heapify(str_list)

    while str_list:
        word = heapq.heappop(str_list)
        answer.append(word[1])
        
    return answer


# solution 2
def solution(strings, n):
    return sorted(strings, key=lambda x: x[n]+x)  # n번째 문자 우선, 그다음 전체 문자열 기준 정렬


"""
lambda 함수 사용법을 잘 익혀두면 좋을 것 같다.
https://velog.io/@euisuk-chung/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%8B%9C%EA%B0%81%ED%99%94-%EB%A7%88%EC%8A%A4%ED%84%B0%ED%95%98%EA%B8%B0-%EB%9E%8C%EB%8B%A4Lambda-%ED%95%A8%EC%88%98
"""