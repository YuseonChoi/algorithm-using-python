""" <가장 큰 수> https://school.programmers.co.kr/learn/courses/30/lessons/42746 """

def solution(numbers):
    answer = ''
    
    # 사전 순으로 더 큰 수가 오도록 정렬
    # 가장 큰 수는 네 자리 수 이하 
    # 6과 34의 경우, 6666 > 34343434
    sort_nums = sorted(list(map(str,numbers)), key = lambda x: x*4, reverse=True)
    answer = ''.join(sort_nums)

    # 000이 아니라 0으로 나와야 함 
    return str(int(answer))