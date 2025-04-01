""" [예상 대진표] https://school.programmers.co.kr/learn/courses/30/lessons/12985 """

# solution 1
def solution(n,a,b):
    round = 1
    while True:
        if (a-1)//2 == (b-1)//2:
            break
        else:
            round+=1
            a = a//2+a%2
            b = b//2+b%2
    return round


# solution 2
def solution(n,a,b):
    answer = 0
    while a!=b:
        a = (a+1)//2
        b = (b+1)//2
        answer+=1
    return answer


# soluton 3
def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()