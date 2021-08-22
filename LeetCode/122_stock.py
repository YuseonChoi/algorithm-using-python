""" 
<주식을 사고팔기 가장 좋은 시점 2> https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

여러 번의 거래로 낼 수 있는 최대 이익을 산출해라.

[input]
[7,1,5,3,6,4]

[output]
7

"""

""" solution-1 그리디 알고리즘 """

class Solution(object):
    def maxProfit(self, prices):
        sum = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                sum += prices[i+1] - prices[i]
        return sum

# a = Solution()
# print(a.maxProfit([7,1,5,3,6,4]))



""" solution-2 파이썬 only """

class Solution(object):
    def maxProfit(self, prices):
        return sum(max(prices[i+1]-prices[i], 0) for i in range(len(prices)-1))