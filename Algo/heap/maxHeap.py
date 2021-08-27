""" <최대힙> """
  
import sys
import heapq as hp

input = sys.stdin.readline
nums = []

while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(nums) == 0:
            print(-1)
        else:
            print(-hp.heappop(nums))
    else:
        hp.heappush(nums, -n)


"""
파이썬 heapq 모듈은 최소 힙만 지원하기 때문에 최대 힙을 구현하려면 음수로 저장한 다음 가장 낮은 수부터 추출해 부호를 변환해야 한다.

"""
