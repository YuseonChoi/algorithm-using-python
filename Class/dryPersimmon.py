"""
<곶감>

[input]
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
3
2 0 3
5 1 2
3 1 4

[output]
362

"""

""" solution-1 """

import sys
input = sys.stdin.readline

# 입력값 받기
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

M = int(input())
for i in range(M):
    a,b,c = map(int, input().split())
    if b == 0:
        for _ in range(c):                                  # 12 39 30 23 11  (원래값)
            grid[a-1].append(grid[a-1].pop(0))              # 23 11 12 39 30  (왼쪽으로 회전)
    else:
        for _ in range(c):
            grid[a-1].insert(0, grid[a-1].pop())            # 30 23 11 12 39  (오른쪽으로 회전)

    
# 모래시계 모양 개수 구하기
sum = 0
start, end = 0, N-1
for i in range(N):
    for j in range(start, end+1):
        sum += grid[i][j]
    if i < N//2:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1
print(sum)
