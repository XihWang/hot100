class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        trace = []
        res = []
        numbool = [False] * n
        def backtrace():
            if len(trace) == n:
                res.append(trace[:])
                return
            for i in range(n):
                if numbool[i] == False:
                    trace.append(nums[i])
                    numbool[i] = True
                    backtrace()
                    trace.pop()
                    numbool[i] = False
        backtrace()
        return res

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         trace = []
#         res = []
#         def backtrace(i, s):
#             if i == n:
#                 res.append(trace[:])
#                 return
#             for x in s:
#                 trace.append(x)
#                 backtrace(i+1, s-{x})
#                 trace.pop()
#         backtrace(0, set(nums))
#         return res