""" <입국 심사> https://chatgpt.com/c/68d229ed-f838-832a-a85f-2f6b3bf29240 """

def solution(n, times):
    left, right = 1, max(times) * n
    answer = right
    
    while left <= right:
        mid = (left + right) // 2  # 현재 가정하는 시간
        total = sum(mid // t for t in times)  # mid 분 동안 처리할 수 있는 인원
        
        if total >= n:  # n명 이상 가능하다면
            answer = mid  # 일단 답 후보 저장
            right = mid - 1  # 더 짧은 시간도 가능한지
        else:
            left = mid + 1  # 시간이 더 필요함
            
    return answer


"""
예를 들어
n = 6, times = [7, 10]

범위 설정
최소 시간 = 1분
최대 시간 = 10 * 6 = 60분

mid = 30분 가정
7분 심사관: 30 // 7 = 4명

10분 심사관: 30 // 10 = 3명

총 7명 → 6명보다 많다 → 30분이면 충분! ⇒ 더 줄여도 될까? right = 29

"""