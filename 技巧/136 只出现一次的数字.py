from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        return res

# from typing import List
# from functools import reduce
# from operator import xor
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         return reduce(xor, nums)

