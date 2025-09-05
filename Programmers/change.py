""" <거스름돈> https://school.programmers.co.kr/learn/courses/30/lessons/12907 """

""" solution 1 - dp 구현 """
def solution(n, money):
    methods = [0]*(n+1)
    methods[0] = 1  # 0원을 만드는 방법 -> 1가지
    
    for m in money:
        for i in range(m, n+1):
            methods[i] = (methods[i] + methods[i-m])
        
    return methods[n] % 1000000007


""" solution 2 - 재귀 구현 (시간초과) """
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
