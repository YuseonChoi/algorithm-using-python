""" <재귀함수를 이용한 이진수 출력> 
재귀 구현 시, 깊이 우선 탐색 개념을 이용해 풀 수 있다.

"""

""" solution-1 반복 구현 """

def transform1(num):
    res = []
    while True:
        tmp = num % 2
        num = num // 2
        if tmp == 0 and num == 0:
            break
        res.insert(0,tmp)
    return res

# N = int(input())
# print(*transform1(N), sep='')



""" solution-2 재귀 구현 """

def transform2(N):
    if N == 0:
        return
    else:
        transform2(N//2)
        print(N%2, end="")

N = int(input())
transform2(N)



"""
19(10진수) -> 10011(2진수)
19/2 = 9/1
9/2 = 4/1
4/2 = 2/0
2/2 = 1/0
1/2 = 0/1

"""