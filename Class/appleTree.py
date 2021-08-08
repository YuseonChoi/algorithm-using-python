""" 
<사과나무(다이아몬드)> 
현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자 안에는 한 그루의 사과나무가 심어져 있다. N의 크기는 항상 홀수이다. 가을이 되어 사과를 수확해야 하는데 현수는 격자판의 사과를 수확할 때 다이아몬드 모양의 격자판만 수확하고 나머지 격자 안의 사과는 새들을 위해서 남겨놓는다. 만약 N이 5이면 아래 그림과 같이 진한 부분의 사과를 수확한다. 현수가 수확하는 사과의 총 개수를 출력하시오.

[input]
첫 줄에 자연수 N(홀수)이 주어진다.
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다.
이 자연수는 각 격자 안에 있는 사과나무에 열린 사과의 개수이다.
각 격자 안의 사과의 개수는 100을 넘지 않는다.

[output]
수확한 사과의 총 개수를 출력합니다.

"""

""" solution-1 """

N = int(input())
apples = []
sum = 0

for _ in range(N):
    a = list(map(int, input().split()))
    apples.append(a)

# 0행~N//2행 까지
start = 0
end = N
for i in range(N//2,0,-1):
    for j in range(start, end):
        sum += apples[i][j]
    start += 1
    end -= 1
sum += apples[0][N//2]

# N//2+1행~N-1(마지막)행까지
start = 1
end = N-1

for i in range(N//2+1, N):
    for j in range(start, end):
        sum += apples[i][j]
    start += 1
    end -= 1

print(sum)
    


""" solution-2 """

N = int(input())
apples = [list(map(int, input().split())) for _ in range(N)]

sum = 0
start = end = N//2

for i in range(N):
    for j in range(start, end+1):
        sum += apples[i][j]
    if i < N//2:
        start -= 1
        end += 1
    else:
        start += 1
        end -= 1

print(sum)