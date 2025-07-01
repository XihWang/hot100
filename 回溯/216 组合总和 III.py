class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        trace = []
        res = []
        def backtrace(start):
            if sum(trace) > n:
                return
            if len(trace) == k and sum(trace) == n:
                res.append(trace[:])
            for i in range(start, 10):
                trace.append(i)
                backtrace(i + 1)
                trace.pop()
        backtrace(1)
        return res