"""
<봉우리>

[input]
5
5 3 7 2 3
3 7 1 6 1
7 2 5 3 4
4 3 6 4 1
8 7 3 5 2

[output]
10

"""

""" solution-1 """

import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
peak = 0  # 봉우리 개수

for i in range(len(grid)):
    grid[i].insert(0,0)
    grid[i].append(0)

grid.insert(0, [0 for _ in range(N+2)])  
grid.append([0 for _ in range(N+2)])


for i in range(1, N+1):
    for j in range(1, N+1):
        num = grid[i][j]
        if num > grid[i-1][j] and num > grid[i+1][j] and num > grid[i][j-1] and num > grid[i][j+1]:
            peak += 1

print(peak)



""" solution-2 Upgrade """

import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
dx = [-1,1,0,0]  # 행에 더해짐
dy = [0,0,-1,1]  # 열에 더해짐
peak = 0  # 봉우리 개수

for i in range(len(grid)):
    grid[i].insert(0,0)
    grid[i].append(0)

grid.insert(0, [0 for _ in range(N+2)])  
grid.append([0 for _ in range(N+2)])


for i in range(1, N+1):
    for j in range(1, N+1):
        if all(grid[i][j] > grid[i+dx[k]][j+dy[k]] for k in range(4)):  # 모든 조건을 만족해야함
            peak += 1

print(peak)