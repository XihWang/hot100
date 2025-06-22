# class Solution(object):
#     def searchRange(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         left = 0
#         right = len(nums) - 1
#         if len(nums) == 0:
#             return [-1, -1]
#         if target > nums[right] or target < nums[left]:
#             return [-1, -1]
#         while left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] == target:
#                 right = mid - 1
#             elif nums[mid] < target:
#                 left = mid + 1
#             elif nums[mid] > target:
#                 right = mid - 1
#         if nums[left] == target:
#             l = left
#             while left < len(nums) and nums[left] == target:
#                 left += 1
#             r = left - 1
#             return [l, r]
#         return [-1, -1]
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(target):
            left = 0
            n = len(nums)
            right = n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        start = lower_bound(target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = lower_bound(target + 1) - 1
        return [start, end]
