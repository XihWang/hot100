class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        n = len(s)
        tmp = [0] * n
        res = 0
        cur = 0
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    j = stack.pop()
                    tmp[j] = tmp[i] = 1
        for i in range(n):
            if tmp[i]:
                cur += 1
            else:
                res = max(res, cur)
                cur = 0
        res = max(res, cur)  # 最后可能还有一轮要比较
        return res

# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         n = len(s)
#         f = [0] * (n+1)
#         for i in range(n):
#             if s[i] == ')':
#                 if i-1>= 0 and s[i-1] == "(":
#                     f[i] = f[i-2] + 2
#                 elif f[i-1] > 0:
#                     if i-f[i-1]-1 >= 0 and s[i-f[i-1]-1] == '(':
#                         f[i] = f[i - f[i - 1] - 2] + 2 + f[i-1]
#         return max(f)
