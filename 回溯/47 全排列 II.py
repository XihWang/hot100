class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        trace = []
        nums = sorted(nums)
        used = [False] * len(nums)
        def backtrace(nums):
            if len(trace) == len(nums):
                res.append(trace[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                if used[i]:
                    continue
                trace.append(nums[i])
                used[i] = True
                backtrace(nums)
                trace.pop()
                used[i] = False

        backtrace(nums)
        return res
