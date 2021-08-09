""" <수 찾기> https://www.acmicpc.net/problem/1920 """

""" solution-1 시간초과, 딕셔너리 사용 """

import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))

dic = {}

for i in M_list:
    if i not in N_list:
        dic[i] = 0
    else:
        dic[i] = 1

for j in dic.values():
    print(j)



""" solution-2 이분탐색 활용, 반복 """

import sys
input = sys.stdin.readline

def binarySearch(num, sorted_list):
    left = 0
    right = len(sorted_list)-1
    
    while left <= right:
        mid = (left+right)//2
        if sorted_list[mid] < num:
            left = mid + 1
        elif sorted_list[mid] > num:
            right = mid-1
        else:
            return 1
    return 0


N = int(input())
N_list = list(map(int, input().split()))
N_sorted = sorted(N_list)

M = int(input())
M_list = list(map(int, input().split()))

for i in range(M):
    print(binarySearch(M_list[i], N_sorted))



""" solution-3 이분탐색 활용, 재귀 """

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)  # 최대 재귀 깊이 설정

def binarySearch(num, sorted_list, left, right):
    
    if left <= right:
        mid = (left+right)//2
        if sorted_list[mid] < num:
            return binarySearch(num, sorted_list, mid+1, right)
        elif sorted_list[mid] > num:
            return binarySearch(num, sorted_list, left, mid-1)
        else:
            return 1
    return 0


N = int(input())
N_list = list(map(int, input().split()))
N_sorted = sorted(N_list)

M = int(input())
M_list = list(map(int, input().split()))

for i in range(M):
    print(binarySearch(M_list[i], N_sorted, 0, len(N_sorted)-1))