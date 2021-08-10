"""
<이분검색>
임의의 N개의 숫자가 입력으로 주어집니다. N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한 개의 수인 M이 주어지면 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는 프로그램을 작성하세요.

[input]
8 32
23 87 65 12 57 32 99 81

[output]
3

"""

""" solution-1 이분탐색 활용 """

def binarySearch(lst, target):
    left, right = 0, len(lst)-1

    while left <= right:
        mid = (left+right)//2
        if lst[mid] < target:
            left = mid + 1
        elif lst[mid] > target:
            right = mid-1
        else:
            return mid + 1
    


N, M = map(int, input().split())
N_list = list(map(int, input().split()))
N_list.sort()  # [12, 23, 32, 57, 65, 81, 87, 99]

print(binarySearch(N_list, M))





