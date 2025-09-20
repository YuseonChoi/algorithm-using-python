""" <k번째 수> https://school.programmers.co.kr/learn/courses/30/lessons/42748 """

def solution(array, commands):
    answer = []
    for i,j,k in commands:
        num = sorted(array[i-1:j])
        answer.append(num[k-1])
    return answer