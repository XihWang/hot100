
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
         # 前缀和 然后变成了121.买卖股票1
         # -2 -1 -4 0 -1 1 2 -3 1
         presum = minpresum =  0
         res = -float('inf')
         for i in nums:
             presum += i
             res = max(res, presum - minpresum)
             minpresum = min(minpresum, presum)
         return res


class Solution:
    # 动态规划
    # 121 股票也可以这个思路
    # f代表以nums[i]结尾的最大子数组和
    # f[0] = nums[0]
    # f[i] = max(f[i - 1], 0) + nums[i]
    # return max(f)
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -float("inf")  # 注意答案可以是负数，不能初始化成 0
        f = 0
        for x in nums:
            # 由于f只和前一个f有关 所以空间上可以优化
            f = max(f, 0) + x
            ans = max(ans, f)
        return ans

