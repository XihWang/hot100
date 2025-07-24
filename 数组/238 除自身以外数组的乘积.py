# 自己的方法 会超时
# from typing import List
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         res = []
#         total = 1
#         for i in range(n):
#             for j in range(i + 1, n):
#                 total = total * nums[j]
#             for j in range(0, i):
#                 total = total * nums[j]
#             res.append(total)
#             total = 1
#
#         return res
#


# from typing import List


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         res = []
#         pre = [1] * n
#         suf = [1] * n
#         for i in range(1, n):
#             pre[i] = pre[i - 1] * nums[i - 1]
#         for i in range(n - 2, -1, -1):
#             suf[i] = suf[i + 1] * nums[i + 1]
#         for i in range(n):
#             res.append(pre[i] * suf[i])
#         return res

# 不用额外的空间
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suf = [1] * n
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]

        pre = 1
        for i, x in enumerate(nums):
            # 此时 pre 为 nums[0] 到 nums[i-1] 的乘积，直接乘到 suf[i] 中
            suf[i] *= pre
            pre *= x

        return suf



