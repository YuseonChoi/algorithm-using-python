"""
<보석과 돌> https://leetcode.com/problems/jewels-and-stones/

J는 보석이며, S는 갖고 있는 돌이다. S에는 보석이 몇 개나 있을까? 대소문자는 구분한다.

[input]
jewels = 'aA', stones = 'aAAbbbb'

[output]
3

"""

""" solution-1 딕셔너리 사용 """

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        cnt = 0
        dic = {}

        # 보석을 key값으로 설정
        for i in jewels:
            dic[i] = 1

        # 돌 안의 보석의 빈도수 계산
        for i in stones:
            if i in dic:
                cnt += 1
        return cnt


class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        dic = {}
        cnt = 0

        # 돌을 key값으로 빈도수 계산
        for i in stones:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        # 보석의 빈도수 합산
        for i in jewels:
            if i in dic:
                cnt += dic[i]

        return cnt
        


""" solution-2 defaultdict 이용 """

from collections import defaultdict

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        d = defaultdict(int)
        cnt = 0

        # 비교 없이 돌의 빈도수 계산
        for i in stones:
            d[i] += 1

        # 비교 없이 보석의 빈도수 합산
        for i in jewels:
            cnt += d[i]
            
        return cnt



""" solution-3 Counter 이용 """

from collections import Counter

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        cnt = 0
        c = Counter(stones)
        
        # Counter({'b': 4, 'A': 2, 'a': 1})
        # Counter는 존재하지 않는 키의 경우 keyError를 발생하는 게 아니라 0을 출력 (딕셔너리와 비교해보기)
        
        for i in jewels:
            cnt += c[i]

        return cnt



""" solution-4 간단한 풀이 """

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        # [True,True,True,False,False,False,False]
        return sum(i in jewels for i in stones)