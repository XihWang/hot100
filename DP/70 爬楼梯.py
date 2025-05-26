# 递归 记忆化搜索
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n+1)
        def dp(i):   # 到第i节台阶有多少方案
            if i <= 1: # 0有一个方法原地不动 1有一个方法 走1格
                return 1
            if memo[i] != 0:
                return memo[i]
            memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]
        return dp(n)

# 直接cache装饰 将输入输出对应存储起来
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         @cache
#         def dp(i):   # 到第i节台阶有多少方案
#             if i <= 1: # 0有一个方法原地不动 1有一个方法 走1格
#                 return 1
#             return dp(i - 1) + dp(i - 2)
#         return dp(n)

# 递推
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         f = [0] * (n + 1)
#         f[0] = f[1] = 1
#         for i in range(2, n+1):
#             f[i] = f[i-1] + f[i-2]
#         return f[n]

# 节约空间的递推
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         f0 = f1 =1
#         for i in range(2, n+1):
#             f0,f1 = f1, f1+f0
#         return f1