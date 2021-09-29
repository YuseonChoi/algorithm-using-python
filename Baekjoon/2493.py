""" <탑> https://www.acmicpc.net/problem/2493 """

""" solution-1 완전탐색 (시간초과) """

import sys

input = sys.stdin.readline

n = int(input())
stack = list(map(int, input().split()))
res = [0]  # 처음은 무조건 0

for i in range(1, len(stack)):
    tmp = 0
    for j in range(i):
        if stack[i] <= stack[j]:
            tmp = j+1
    res.append(tmp)

print(res)



""" solution-2 스택 활용 """

n = int(input())
nums = list(map(int, input().split()))
stack = []   # [ [인덱스, 탑의 높이] ]
res = []     # 수신 탑 인덱스 저장

for i in range(n):
    while stack:
        if stack[-1][1] > nums[i]:
            res.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:  # 스택이 비면 수신할 탑이 없음
        res.append(0)
    stack.append([i, nums[i]])

print(" ".join(map(str, res)))

