# 下面的方法是错误的！！ 因为
# from typing import List
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n = len(nums)
#         if n == 1:
#             return True
#         if nums[0] == 0:
#             return False
#         i = 0
#         for j in range(nums[i], 0, -1):
#             if i + j < n and nums[i + j] > 0:
#                 i = i + j
#             elif i + j == n - 1:
#                 return True
#         return False


from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farthest = 0  # 记录最远可以到达的位置

        for i in range(n):
            if i > farthest:  # 如果当前位置超出最远可到达位置，则无法继续
                return False
            farthest = max(farthest, i + nums[i])  # 更新最远可到达位置
            if farthest >= n - 1:  # 如果最远可到达位置已经覆盖最后一个索引，直接返回 True
                return True




