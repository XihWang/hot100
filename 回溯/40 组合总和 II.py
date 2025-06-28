class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        trace = []
        candidates = sorted(candidates)
        def backtrace(start, total):
            if total == target:
                res.append(trace[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i-1] == candidates[i]:
                    continue
                total = total + candidates[i]
                trace.append(candidates[i])
                backtrace(i + 1, total)
                total = total - candidates[i]
                trace.pop()
        backtrace(0,0)
        return res
