""" <전화번호 문자 조합> https://leetcode.com/problems/letter-combinations-of-a-phone-number/ 

[input]
digits = "23"

[output]
["ad","ae","af","bd","be","bf","cd","ce","cf"]

"""

""" solution-1 product 모듈 이용 """

# product: 여러 집합들 간 하나씩 뽑아 조합 생성
# a = [1,2,3]
# b = ['a','b','c']
# product(a,b) -> [(1,'a'),(1,'b'),(1,'c'),(2,'a'),...]

from itertools import product

dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

class Solution(object):
    def letterCombinations(self, digits):
        lst = []  # 번호별 문자를 담을 리스트
        res = []  # 최종 리턴값. 조합 가능한 문자를 담을 리스트
        
        # 예외처리
        if not digits:
            return res

        for i in digits:
            if i in dic:
                lst.append(dic[i])
        tmp = list(product(*lst))
        # print(lst) -> ['abc', 'def']
        # print(*lst) -> abc def
        # print(tmp) -> [('a', 'd'), ('a', 'e'), ('a', 'f'), ('b', 'd'), 
        # ('b', 'e'), ('b', 'f'), ('c', 'd'), ('c', 'e'), ('c', 'f')]
        for i in tmp:
            res.append("".join(i))
        # print(res) -> ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        return res


a = Solution()
print(a.letterCombinations("23"))



""" solution-2 모든 조합 탐색 """

dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

class Solution(object):
    def letterCombinations(self, digits):
        def dfs(index, path):

            # 끝까지 탐색하면 백트래킹
            if len(path) == len(digits):
                res.append(path)
                return
        
            # 입력값 자릿수 단위 반복
            for i in range(index, len(digits)):
                # 숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]:
                    dfs(i+1, path + j)

        # 예외처리
        if not digits:
            return []

        res = []
        dfs(0,"") 

        return res

a = Solution()
print(a.letterCombinations("23"))