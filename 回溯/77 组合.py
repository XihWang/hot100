class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        trace = []
        def backtrace(start):
            if len(trace) == k:
                res.append(trace[:])
                return
            for i in range(start, n + 1):
                trace.append(i)
                backtrace(i + 1)
                trace.pop()
        backtrace(1)
        return res

# class Solution(object):
#     def __init__(self):
#         self.res = []
#         self.trace = []
#     def combine(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         self.backtrace(n, k, 1)
#         return self.res
#
#
#     def backtrace(self, n, k, start):
#         if len (self.trace) == k:
#             self.res.append(list(self.trace))
#             return
#         for i in range(start, n + 1):
#             self.trace.append(i)
#             self.backtrace(n, k, i + 1)
#             self.trace.pop()
