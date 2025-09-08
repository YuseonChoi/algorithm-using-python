""" <정수 삼각형> https://school.programmers.co.kr/learn/courses/30/lessons/43105?gad_source=1&gad_campaignid=22681436564&gbraid=0AAAAAC_c4nDGczD64bX4kfw7ydV-CV7Ap&gclid=CjwKCAjw2vTFBhAuEiwAFaScwuxsfvLRCPR5sxnSui1buvbyD6e5fUj6AcICtqYr1MjVdH8zt2nYDBoCpgsQAvD_BwE """

""" solution1 """
def solution(triangle):
    N = len(triangle)
    
    for i in range(1,N):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j]
            elif j == i:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
            else:
                triangle[i][j] = max(
                    triangle[i][j] + triangle[i-1][j-1],
                    triangle[i][j] + triangle[i-1][j]
                )
        
    return max(triangle[N-1])

