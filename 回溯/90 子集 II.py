class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        trace = []
        nums = sorted(nums)
        def backtrace(nums, start):
            res.append(trace[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                trace.append(nums[i])
                backtrace(nums, i + 1)
                trace.pop()

        backtrace(nums, 0)
        return res