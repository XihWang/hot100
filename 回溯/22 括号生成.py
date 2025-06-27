class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m = 2 * n
        trace = [''] * m
        res = []
        def backtrace(i, open):  # open是（的数目 最后是n个
            if i == m:
                res.append(''.join(trace))
                return
            if open < n:
                trace[i] = '('
                backtrace(i + 1, open + 1)
            if i - open < open: # 除了（就是） 当）的数目少于（的时候 加）
                trace[i] = ')'
                backtrace(i + 1, open)
        backtrace(0, 0)
        return res

# 这两种写法是相同的 只是预先初始化trace的话 后续都直接覆盖了 所以不需要pop
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         m = 2 * n
#         trace = []
#         res = []
#         def backtrace(i, open):
#             if i == m:
#                 res.append(''.join(trace))
#                 return
#             if open < n:
#                 trace.append('(')
#                 backtrace(i + 1, open + 1)
#                 trace.pop()
#             if i - open < open:
#                 trace.append(')')
#                 backtrace(i + 1, open)
#                 trace.pop()
#         backtrace(0, 0)
#         return res

