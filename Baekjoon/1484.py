""" <다이어트> https://www.acmicpc.net/problem/1484 """

import sys
input = sys.stdin.readline

G = int(input())

CW = [i for i in range(1,100001)]
MW = [i for i in range(1,100001)]
N, M = 100000, 100000
left, right = 0, 0
res = []

while left < N and right < M:

    # G킬로그램 = 현재 몸무게의 제곱 - 기억하고 있던 몸무게의 제곱
    # G = CW^2 - MW^2 => (CW + MW)(CW - MW)
    
    tmp = (CW[left] + MW[right]) * (CW[left] - MW[right])

    # tmp < G, G가 나오기 위해서는 반드시 CW[left]가 더 커야 한다.
    # tmp > G, tmp를 줄여줌으로써 tmp가 G에 근접하게 된다. 

    if tmp == G:
        res.append(CW[left])
    elif tmp < G:
        left += 1
        continue
    right += 1

if not res:
    print(-1)
else:
    print(*res, sep='\n')