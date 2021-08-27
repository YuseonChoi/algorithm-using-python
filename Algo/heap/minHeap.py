""" <최소힙> """

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
            print(hp.heappop(nums))
    else:
        hp.heappush(nums, n)
