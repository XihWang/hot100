class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = [0] * n   # 第0行放在col[0]列上
        onpath = [False] * n
        m = n * 2 - 1
        diag1 = [False] * m
        diag2 = [False] * m # 注意这里也是2*n -1个  (-n+1, n-1) 总共也是m个数
        res = []
        def backtrace(r):
            if r == n:
                res.append(['.' * c + 'Q' + '.' * (n - 1 - c) for c in col])
            for c in range(n):  # 本质上是对n的一个排列  但是要满足对角线的约束
                if not onpath[c] and not diag1[r+c] and not diag2[r-c]:  # 对于其他语言需要加n-1 py不需要
                    col[r] = c
                    onpath[c] = diag1[r+c] = diag2[r-c] = True
                    backtrace(r + 1)
                    onpath[c] = diag1[r+c] = diag2[r-c] = False
        backtrace(0)
        return res


# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         col = [0] * n
#         res = []
#         def backtrace(r, s):
#             if r == n:
#                 res.append(['.' * c + 'Q' + '.' * (n-1-c) for c in col])
#                 return
#             for c in s:
#                 if all(r+c != R + col[R] and r-c != R-col[R] for R in range(r)):
#                     col[r] = c
#                     backtrace(r+1, s-{c})
#         backtrace(0, set(range(n)))
#         return res


