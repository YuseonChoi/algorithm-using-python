""" <암기왕> https://www.acmicpc.net/problem/2776 """

# target 값이 lst안에 들어있는지 판별하는 함수
# 들어있다면 1 출력, 들어있지 않다면 0 출력
def search(lst, target):
    left = 0
    right = len(lst)-1

    while left <= right:
        mid = (left+right)//2
        if lst[mid] < target:
            left = mid + 1
        elif lst[mid] > target:
            right = mid-1
        else:
            return 1
    return 0


T = int(input())

for i in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))
    M = int(input())
    M_list = list(map(int, input().split()))
    N_list.sort()

    for j in M_list:
        print(search(N_list,j))