""" <배열의 K번째 큰 요소> https://leetcode.com/problems/kth-largest-element-in-an-array/ """

""" solution-1 heapq 모듈 이용 """

import heapq as hp

class Solution(object):
    def findKthLargest(self, nums, k):
        res = []
        for i in nums:
            hp.heappush(res, -i)
        
        for _ in range(k-1):
            hp.heappop(res)
        
        return -hp.heappop(res)

# a = Solution()
# print(a.findKthLargest([3,2,1,5,6,4], 2))
# print(a.findKthLargest([3,2,3,1,2,4,5,5,6], 4))



""" solution-2 heapq 모듈의 heapify 이용 """

import heapq as hp

class Solution(object):
    def findKthLargest(self, nums, k):
        # 모든 값을 꺼내 push할 필요 없이 한 번에 처리
        hp.heapify(nums)

        for _ in range(len(nums)-k):
            hp.heappop(nums)
        
        return hp.heappop(nums)



""" solution-3 heapq 모듈의 nlargest 이용 """

import heapq as hp

class Solution(object):
    def findKthLargest(self, nums, k):
        # k번째 만큼 큰 값이 가장 큰 값부터 순서대로 리스트로 리턴
        return hp.nlargest(k, nums)[-1]

# 참고로 nsmallest()을 사용하면 동일한 방식으로 n번째 작은 값을 구할 수 있다.



""" solution-4 정렬을 이용한 풀이 """

class Solution(object):
    def findKthLargest(self, nums, k):
        return sorted(nums, reverse=True)[k-1]

# 모든 방식의 실행 속도에 큰 차이는 없으나, '정렬'이 가장 빠르다..
# 추가, 삭제가 빈번할 때는 heapq를 이용한 힙 정렬이 유용하지만 입력값이 고정되어 있을 때는 한 번 정렬하는 것으로 충분하다.