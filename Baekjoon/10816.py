""" <숫자 카드 2> https://www.acmicpc.net/problem/10816 

숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

[input]
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

[output]
3 0 0 1 2 0 0 2

"""

""" solution-1 이진탐색, 딕셔너리 사용 """ 

import sys
input = sys.stdin.readline

def binarySearch(nums, target):
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left+right)//2
        if nums[mid] < target:
            left = mid+1
        elif nums[mid] > target:
            right = mid-1
        else:
            return dic[target]
    return 0

# list_count는 시간복잡도가 O(n)이기 때문에 시간초과 발생
# 이분탐색 사용시, 해당 리스트는 정렬된 상태여야 함


# input
N = int(input())
N_list = list(map(int, input().split()))
N_sorted = sorted(N_list)

M = int(input())
M_list = list(map(int, input().split()))

# dict - N_sorted 빈도수 구하기
global dic
dic = {}
for i in N_sorted:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

for i in M_list:
    print(binarySearch(N_sorted, i), end=' ')



""" solution-2 딕셔너리만 사용 """

import sys
input = sys.stdin.readline

_ = int(input())
N_list = list(map(int, input().split()))

_ = int(input())
M_list = list(map(int, input().split()))

dic = {}

# 이분탐색 X, 굳이 정렬할 필요 없음
for i in N_list:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

# for i in M_list:
#     if i in dic:
#         print(dic[i], end=' ')
#     else:
#         print(0, end=' ')

print(' '.join(str(dic[i]) if i in dic else '0' for i in M_list))



""" solution-3 Collections 라이브러리의 Counter 함수 사용 """

import sys
from collections import Counter
input = sys.stdin.readline

_ = int(input())
N_list = list(map(int, input().split()))

_ = int(input())
M_list = list(map(int, input().split()))

C = Counter(N_list)

# print(C)
# Counter({10: 3, 3: 2, -10: 2, 6: 1, 2: 1, 7: 1})

print(' '.join(f'{C[i]}' if i in C else '0' for i in M_list))