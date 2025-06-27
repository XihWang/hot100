class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        trace = []
        total = 0
        def backtrace(total, start):
            if total > target:
                return
            if total == target:
                res.append(trace[:])
                return
            for i in range(start, len(candidates)):
                total = total + candidates[i]
                trace.append(candidates[i])
                backtrace(total, i)
                trace.pop()
                total = total - candidates[i]

        backtrace(total,0 )
        return res


