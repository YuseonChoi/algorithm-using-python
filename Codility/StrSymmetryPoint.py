"""
문자열을 배열에 적용 가능함..
문자열 길이가 짝수인 걸 먼저 쳐내는 거랑 n//2 반환하는 걸 생각 못 함..
"""

def solution(S):
    n = len(S)
    mid = len(S)//2
    
    # 문자열 길이가 짝수면 -1 반환
    if n % 2 == 0:
        return -1

    for i in range(mid):
        if S[i] != S[n-i-1]:
            return -1
    return mid