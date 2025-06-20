from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def is_blue(i):
            end = nums[-1]
            if nums[i] > end:
                return nums[i] >= target and target > end
            else:
                return target > end or target < nums[i]
        n = len(nums)
        left = 0
        right = n - 2
        while left <= right:
            mid = left + (right - left) // 2
            if is_blue(mid):
                right = mid + 1
            else:
                left = mid - 1
        if left == len(n) + 1 or nums[left] != target:
            return -1
        return left

