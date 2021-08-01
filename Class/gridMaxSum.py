"""
<격자판 최대합>

5*5 격자판에 숫자가 적혀있습니다.
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 합을 출력합니다. 

"""

""" solution-1 """

N = int(input())
grid = []

for _ in range(N):
    g = list(map(int, input().split()))
    grid.append(g)

sum_list = []  # 각각의 합들을 담을 리스트


# 가로 방향으로 더하기
for i in range(N):
    R_sum = 0
    for j in range(N):
        R_sum += grid[i][j]
    sum_list.append(R_sum)

# 세로 방향으로 더하기
for i in range(N):
    C_sum = 0
    for j in range(N):
        C_sum += grid[j][i]
    sum_list.append(C_sum)

# 대각선 방향으로 더하기
D1_sum = 0
D2_sum = 0
## 왼쪽 끝 대각선
for i in range(N):
    D1_sum += grid[i][i]
sum_list.append(D1_sum)
## 오른쪽 끝 대각선
for i in range(N):
    D2_sum += grid[N-1-i][i]
sum_list.append(D2_sum)

print(max(sum_list))




