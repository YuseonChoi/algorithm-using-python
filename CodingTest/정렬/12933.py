""" [정수 내림차순으로 배치하기] https://school.programmers.co.kr/learn/courses/30/lessons/12933?language=python3 """

# solution 1
def solution(n):
    answer = []
    num_str = str(n)
    for s in num_str:
        answer.append(int(s))
    answer.sort(reverse=True)
    
    result = ''.join(map(str, answer))
    
    return int(result)


# solution 2
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))