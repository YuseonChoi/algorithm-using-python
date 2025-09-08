""" <최적의 행렬 곱셈> """


def solution(matrix_sizes):
    n = len(matrix_sizes)
    dp = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 0
    
    for gap in range(1,n):
        for i in range(n-gap):
            j = i + gap
            for k in range(i,j):
                cost = dp[i][k] + dp[k+1][j] \
                       + matrix_sizes[i][0] \
                       * matrix_sizes[k][1] \
                       * matrix_sizes[j][1]
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n-1]

print(solution([[5,3],[3,10],[10,6]]))