"""
[두 개의 수로 특정 값 만들기]
양의 정수로 이루어진 리스트 arr와 정수 target이 주어졌을 때,
이 중에서 합이 target인 두 수가 arr에 있는지 찾고,
있으면 True, 없으면 False를 반환하는 solution() 함수를 작성하시오.
"""

# solution 1 - 무작정 더하며 찾는 방식은 연산의 효율이 떨어짐
def solution(arr, target):
    dic = {}
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            dic[arr[i]+arr[j]] = True

    if target in dic.keys():
        return True

    return False


# solution 2
def solution(arr, target):
    # 해시 테이블 생성 및 초기화
    hash = [0] * (target+1)
    # arr의 각 원소를 키로 해시 테이블 만듦
    for num in arr:
        if num <= target:
            hash[num] = 1

    for num in arr:
        # target 보다 더 큰 값은 답이 될 수 없음
        if (num >= target):
            continue
        # arr에 중복되는 원소는 존재하지 않음
        if ((target - num) == num):
            continue
        # 두 수의 합이 target을 만들어낼 수 있다면 True 반환
        if (hash[target-num]):
            return True
    # 두 수의 합으로 target을 만들 수 없다면 False 반환
    return False


## test case 1
arr = [1,2,3,4,8]
target = 6

## test case 2
arr = [2,3,5,9]
target = 10

print(solution(arr, target))