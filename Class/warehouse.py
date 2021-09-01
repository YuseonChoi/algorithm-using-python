""" <창고정리> """

""" solution-1 """

import sys
input = sys.stdin.readline

def wareHouse(lst, n):
    for _ in range(n):
        lst[lst.index(max(lst))] -= 1
        lst[lst.index(min(lst))] += 1
    return max(lst)-min(lst)


l = int(input())
lst = list(map(int, input().split()))
n = int(input())

print(wareHouse(lst, n))

