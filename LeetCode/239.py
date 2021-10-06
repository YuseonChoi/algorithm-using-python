""" <최대 슬라이딩 윈도우> https://leetcode.com/problems/sliding-window-maximum/ 

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

"""

""" solution-1 브루트 포스로 계산 """

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return nums

        r = []
        for i in range(len(nums)-k+1):
            r.append(max(nums[i:i+k]))   
        return r


nums = [1,3,-1,-3,5,3,6,7]
k = 3

a = Solution()
print(a.maxSlidingWindow(nums, k))



""" solution-2 큐를 이용한 최적화 """

# from collections import deque

# class Solution(object):
#     def maxSlidingWindow(self, nums, k):
#         results = []
#         window = deque()
#         current_max = float('-inf')   # 음의 무한대
#         for i,v in enumerate(nums):
#             window.append(v)
#             if i < k-1:
#                 continue
        
#             # 새로 추가된 값이 기존 최댓값보다 큰 경우 교체
#             if current_max == float('-inf'):
#                 current_max = max(window)
#             elif v > current_max:
#                 current_max = v
            
#             results.append(current_max)

#             # 최댓값이 윈도우에서 빠지면 초기화
#             if current_max == window.popleft():
#                 current_max = float('-inf')

#         return results
        

# nums = [1,3,-1,-3,5,3,6,7]
# k = 3

# a = Solution()
# print(a.maxSlidingWindow(nums, k))
        
