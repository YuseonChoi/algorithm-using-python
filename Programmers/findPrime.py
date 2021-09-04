""" <소수 찾기> https://programmers.co.kr/learn/courses/30/lessons/42839 """

""" solution-1 itertools 모듈 사용 """

from itertools import permutations

# 소수 판별 함수 - 에라토스테네스의 체
def isPrime(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, int(num**1/2)+1):
            if num % i == 0:
                return False
        return True
    

def solution(numbers):
    nums = []    # 숫자를 담을 리스트
    cnt = 0      # 소수의 개수 
    for i in range(1,len(numbers)+1):
        for j in list(map(''.join, permutations(numbers, i))):
            nums.append(int(j))
    
    for i in set(nums):
        if isPrime(i):
            cnt += 1

    return cnt


# print(solution('17'))
# print(solution('011'))
