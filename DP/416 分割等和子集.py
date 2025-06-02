class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numsum = sum(nums)
        if numsum % 2 == 1:
            return False
        weight = numsum / 2
        n = len(nums)
        @cache
        def dp(i, c):
            if c == 0:
                return True
            if i < 0 or c < 0:
                return False
            return dp(i - 1, c) or dp(i - 1, c - nums[i])
        res = dp(n - 1, weight)
        return res
