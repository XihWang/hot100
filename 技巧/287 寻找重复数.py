# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         hash = 0

#         for num in nums:
#             if (hash & (1 << num)) != 0:
#                 return num
#             hash |= (1 << num)

#         return None

# 二分查找法
# from typing import List
#
#
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         min_value = 1
#         max_value = len(nums)
#         while min_value < max_value:
#             mid = (min_value + max_value) // 2
#
#             cnt = sum(min_value <= i <= mid for i in nums)
#             if cnt > mid - min_value + 1:
#                 max_value = mid
#             else:
#                 min_value = mid + 1
#         return min_value

# 快慢指针法
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break
        ptr = 0
        while ptr != slow:
            slow = nums[slow]
            ptr = nums[ptr]
        # 有两个以上入度的地方就是环的入口，也就是重复的数
        return ptr



