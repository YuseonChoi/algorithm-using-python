""" [K번째 수] https://school.programmers.co.kr/learn/courses/30/lessons/42748 """

# solution 1
def solution(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

# solution 2
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))