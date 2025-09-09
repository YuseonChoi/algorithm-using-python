""" <올바른 괄호의 개수> https://school.programmers.co.kr/learn/courses/30/lessons/12929 """

def solution(n):
        
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2,n+1):
        for j in range(i):
            dp[i] += dp[i-j-1] * dp[j]

    return dp[n]

print(solution(4))