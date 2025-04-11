"""
[계수 정렬 구현하기]
인자로 받은 문자열 s를 계수 정렬로 정렬하여 반환하는 함수를 구현하세요.
"""

# solution 1
def solution(s):
    str_list = [i for i in s]
    answer = sorted(str_list, key=lambda x:ord(x))
    return ''.join(answer)

    
# solution 2 - 계수 정렬 풀이
def solution(s):
    counts = [0]*26  # 알파벳 개수만큼 빈도수 배열 생성
    
    # 문자열의 각 문자에 대한 빈도수를 빈도수 배열에 저장
    for c in s:
        counts[ord(c)-ord("a")]+=1
        
    sorted_str = ""
    for i in range(26):
        sorted_str += chr(i+ord("a")) * counts[i]
        
    return sorted_str
        
    
# test case 1
s = "hello"

# test case 2
s = "algorithm"

print(solution(s))