""" <카펫> https://programmers.co.kr/learn/courses/30/lessons/42842 """

""" solution-1 약수로 풀기 """

def solution(brown, yellow):
    target = brown + yellow
    nums = []

    # target의 약수 구하기
    for i in range(1, target+1):
        if i > int(target**0.5):
            break
        if target % i == 0:
            nums.append([target//i, i])

    for n in nums:
        val = 2*(n[0]-2) + 2*n[1]
        if val == brown:
            return n

# print(solution(10,2))
# print(solution(24,24))
# print(solution(8,1))



""" solution-2 약수로 풀기, 코드 간소화 """

def solution(brown, yellow):
    target = brown + yellow
    for i in range(3, int(target ** 0.5) + 1):
        if target%i == 0 and 2 * (target//i + i-2) == brown:
            return [target//i, i]