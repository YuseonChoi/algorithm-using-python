"""
[정렬이 완료된 두 배열 합치기]
이미 정렬이 완료되어 있는 두 배열 arr1, arr2을 받아
병합 정렬하는 함수를 구현하세요.
"""

def solution(arr1, arr2):
    merged = []  # 정렬된 배열을 저장할 리스트 생성
    i, j = 0, 0  # 두 배열의 인덱스 초기화
    
    # 두 배열을 순회하며 정렬된 배열을 생성
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
            
    # arr1이나 arr2 중 남아 있는 원소들을 정렬된 배열 뒤에 추가
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    
    return merged
    
    
# test case 1 - [1,2,3,4,5,6]
arr1 = [1,3,5]
arr2 = [2,4,6]

# test case 2 - [1,2,3,4,5,6]
arr1 = [1,2,3]
arr2 = [4,5,6]

print(solution(arr1, arr2))
