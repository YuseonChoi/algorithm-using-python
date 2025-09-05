""" <거스름돈> https://school.programmers.co.kr/learn/courses/30/lessons/12907 """

""" solution 1 - dp 구현 """
def solution(n, money):
    methods = [0]*(n+1)
    methods[0] = 1  # 0원을 만드는 방법 -> 1가지
    
    for m in money:
        for i in range(m, n+1):
            methods[i] = (methods[i] + methods[i-m])
        
    return methods[n] % 1000000007


""" solution 2 - 재귀 구현 (시간초과)
1. n=5, money=[1,2,5]
    - 가장 큰 동전은 5 → 최대 1개까지 사용 가능.
    - case1: 5를 0개 사용 → solution(5, [1,2])
    - case2: 5를 1개 사용 → solution(0, [1,2])
2. case2에서 n=0이므로 경우의 수 1.
3. case1 → solution(5, [1,2])
    - 가장 큰 동전은 2 → 최대 2개까지 사용 가능.
    - case1-1: 2를 0개 사용 → solution(5, [1]) → 1개 (1*5)
    - case1-2: 2를 1개 사용 → solution(3, [1]) → 1개 (2+1*3)
    - case1-3: 2를 2개 사용 → solution(1, [1]) → 1개 (2*2+1)
    총 3개 경우.
4. 최종 답 = case1(3) + case2(1) = 4가지 방법.
"""
def solution(n, money):
    if n == 0:
        return 1
    
    if len(money) == 1:
        if n%money[0] == 0:
            return 1
        else:
            return 0
    
    answer = 0
    q = n // money[-1]
    for i in range(0, q+1):
        answer += solution(n-money[-1]*i, money[:-1])

    return answer

print(solution(5,[1,2,5]))


