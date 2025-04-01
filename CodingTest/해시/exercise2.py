"""
[문자열 해싱을 이용한 검색 함수 만들기]
문자열 리스트 string_list와 쿼리 리스트 query_list가 있을 때
각 쿼리 리스트에 있는 문자열이 string_list의 문자열 리스트에 있는지
여부를 확인해야 합니다.

문자열이 있으면 True, 없으면 False가 됩니다.
각 문자열에 대해서 문자열의 존재 여부를 리스트 형태로 반환하세요.
"""

# solution 1 
def solution(string_list, query_list):
    dic = {}
    answer = []
    for s in string_list:
        dic[s]=True
    
    for q in query_list:
        if q in dic.keys():
            answer.append(True)
        else:
            answer.append(False)

    return answer


# solution 2
## polynomial hash를 구현한 부분 (polynomial rolling method)
def polynomial_hash(str):
    p = 31
    m = 1_000_000_007  # 버킷 크기
    hash_value = 0

    for char in str:
        hash_value = (hash_value*p + ord(char)) % m  # ord는 문자열을 받아 유니코드 정수로 반환
    return hash_value


def solution(string_list, query_list):
    # string_list의 각 문자열에 대해 다항 해시값을 계산함
    hash_list = [polynomial_hash(str) for str in string_list]

    # query_list의 각 문자열이 string_list에 있는지 확인
    result = []
    for query in query_list:
        query_hash = polynomial_hash(query)
        if query_hash in hash_list:
            result.append(True)
        else:
            result.append(False)
    return result


print(solution(["apple", "banana", "cherry"], ["banana", "kiwi", "melon", "apple"]))

"""
solution 2의 경우, 문자열 비교가 아니라 해싱 함수를 통해 변환된 정수와 비교하기 때문에,
문자열이 길어지거나 데이터가 많은 상황에서, soluton 1에 비해 메모리를 아끼면서 더 빠르게 동작할 수 있음.
단점으로, 해싱 충돌이 일어날 수 있지만, 메르센 소수를 이용한 다항 해싱 함수를 사용해 충돌 가능성을 최소화하였음.
"""