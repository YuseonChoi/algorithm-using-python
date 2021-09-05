""" <구명보트> https://programmers.co.kr/learn/courses/30/lessons/42885 """

""" solution-1 시간초과, O(n) """

def solution(people, limit):
    cnt = 0   # 구명보트 수
    people = sorted(people)
    while people:
        if len(people) == 1:
            cnt += 1
            break
        if people[0] + people[-1] > limit:
            people.pop()
            cnt += 1
        else:
            people.pop(0)
            people.pop()
            cnt += 1
    return cnt

print(solution([70, 50, 80, 50], 100))   # [50,50,70,80]
print(solution([70, 80, 50], 100))



""" solution-2 deque 이용 """

from collections import deque

def solution(people, limit):
    cnt = 0
    dq = deque(sorted(people))

    while dq:
        first = dq.popleft()  # 첫 번째 값
        if not dq:
            return cnt + 1
        last = dq.pop()  # 마지막 값
        if first + last > limit:
            dq.appendleft(first)
        cnt += 1
    return cnt



""" solution-3 간단한 풀이 """

def solution(people, limit):
    people = sorted(people)
    cnt = 0  

    i, j = 0, len(people)-1

    while i <= j:
        cnt += 1
        if people[i] + people[j] <= limit:
            i += 1
        j-= 1
    return cnt






