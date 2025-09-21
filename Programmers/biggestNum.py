""" <가장 큰 수> https://school.programmers.co.kr/learn/courses/30/lessons/42746 """

def solution(numbers):
    answer = ''
    
    sort_nums = sorted(list(map(str,numbers)), key = lambda x: x*4, reverse=True)
    answer = ''.join(sort_nums)

    return str(int(answer))