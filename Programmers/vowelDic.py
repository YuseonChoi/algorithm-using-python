""" <모음사전> https://programmers.co.kr/learn/courses/30/lessons/84512 """

""" solution-1 product 모듈 이용 """

from itertools import product  # 중복순열

def solution(word):
    lst = list()

    for i in range(1,6):
        for j in product(['A','E','I','O','U'], repeat = i):
            lst.append(''.join(j))
    lst.sort()  # 문자정렬
    return lst.index(word)+1



""" solution-2 한줄코딩 """

from itertools import product

# lambda를 이용한 solution 함수
solution = lambda word: sorted([''.join(j) for i in range(5) for j in product('AEIOU', repeat=i+1)]).index(word)+1

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))
