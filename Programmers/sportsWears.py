""" <체육복> https://programmers.co.kr/learn/courses/30/lessons/42862 """

""" solution-1 set 이용 """

def solution(n, lost, reserve):
    # 여벌 체육복이 있는 학생이 도난당했을 때 경우 제외
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    # new_reserve = [i for i in reserve if i not in lost]
    # new_lost = [i for i in lost if i not in reserve]

    for i in new_lost:
        if i-1 in new_reserve:
            new_reserve.remove(i-1)
        elif i+1 in new_reserve:
            new_reserve.remove(i+1)
        else:
            n-=1
    return n
    
# print(solution(5, [2, 4], [1, 3, 5]))
# print(solution(5,[2, 4],[3]))
# print(solution(3, [3], [1]))