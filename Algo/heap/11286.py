""" <절댓값 힙> https://www.acmicpc.net/problem/11286 """

""" solution-1 """

import heapq as hp
import sys

input = sys.stdin.readline
res = list()

for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if len(res) == 0:
            print(0)
        else:
            print(hp.heappop(res)[1])
    else:
        hp.heappush(res, (abs(n),n))
    
# heap은 튜플로 구성했을 때 맨 앞 숫자만 가지고 정렬한다.
# 리스트 res에서 튜플로 묶어진 원소들 중에 인덱스 번호가 1인 원소를 출력한다.
