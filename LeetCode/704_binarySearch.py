"""
<이진 검색>  https://leetcode.com/problems/binary-search/

정렬된 nums를 입력받아 이진 검색으로 target에 해당하는 인덱스를 찾아라.
target 값이 nums 안에 존재하지 않으면 -1을 반환하라.

이진검색 : 정렬된 데이터 집합을 이분화하면서 탐색하는 방법

"""

""" solution-1 이진검색 X, 인덱스 풀이 """

class Solution1_1(object):
    def search(self, nums, target):
        for i in nums:
            if i == target:
                return nums.index(target)
        return -1

class Solution1_2(object):
    def search(self, nums, target):
        try:
            return nums.index(target)
        except:
            return -1


# nums = [-1,0,3,5,9,12]
# target = 9

# a = Solution1_1()
# print(a.search(nums, target))



""" solution-2 이진검색 구현, 반복 풀이 """

class Solution2(object):
    def search(self, nums, target):
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right)//2
            
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1



""" solution-2 이진검색 구현, 재귀 풀이 """

class Solution(object):
    def search(self, nums, target):
        def binary_search(left, right):
            mid = (left+right)//2
            
            if left <= right:
                if nums[mid] < target:
                    return binary_search(mid+1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid-1)
                else:
                    return mid
            return -1

        return binary_search(0, len(nums)-1)  # search() 함수의 return문
        


""" solution-3 이진 검색 모듈 """

import bisect

class Solution(object):
    def search(self, nums, target):
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            # 값이 존재하지 않는 경우 계속 찾으려 하기 때문에 index < len(nums) 조건문을 설정한다.
            return index
        else:
            return -1


""" 참고 https://lioliolio.github.io/python-bisect-module/ """


