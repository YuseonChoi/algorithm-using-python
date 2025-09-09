""" <올바른 괄호의 개수> https://school.programmers.co.kr/learn/courses/30/lessons/12929 """

def solution(n):
        
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2,n+1):
        for j in range(i):
            print(i, i-j-1, j, dp)
            dp[i] += dp[i-j-1] * dp[j]

    return dp[n]

print(solution(4))

# 입력 : 4
# 2 1 0 [1, 1, 0, 0, 0]
# 2 0 1 [1, 1, 1, 0, 0]
# 3 2 0 [1, 1, 2, 0, 0]
# 3 1 1 [1, 1, 2, 2, 0]
# 3 0 2 [1, 1, 2, 3, 0]
# 4 3 0 [1, 1, 2, 5, 0]
# 4 2 1 [1, 1, 2, 5, 5]
# 4 1 2 [1, 1, 2, 5, 7]
# 4 0 3 [1, 1, 2, 5, 9]
# 출력 : 14