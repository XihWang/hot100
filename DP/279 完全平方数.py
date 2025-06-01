
# 时间爆了
# class Solution:
#     def numSquares(self, n: int) -> int:
#         memo = [0] * (n+1)
#         def dp(n):
#             if n in [i*i for i in range(1,floor(sqrt(n)) + 1)]:
#                 return 1
#             if memo[n] != 0:
#                 return memo[n]
#             memo[n] = 1 + min(dp(n - i*i) for i in range(1,floor(sqrt(n)) + 1))
#             return memo[n]
#         return dp(n)


# 方法1 dp代表整数n的最少数量 然后分割成小任务
class Solution:
    def numSquares(self, n: int) -> int:
        @cache
        def dp(n):
            if n in [i*i for i in range(1,isqrt(n) + 1)]:
                return 1
            res = 1 + min(dp(n - i*i) for i in range(1,isqrt(n) + 1))
            return res
        return dp(n)


# 方法二 注意这里dp必须放到外面来 # 写在外面，多个测试数据之间可以共享，减少计算量
# dp代表i个物品 容量是c的完全背包问题  弄满c的最少个i的数量
# @cache
# def dp(i, c):
#     if i == 0:  # 这题分解的数字是从 1 开始的，不是从 0 开始。所以递归到 i=0 的时候就结束了。
#         return 0 if c == 0 else inf
#     if i*i > c:
#         return dp(i-1, c)
#     return min(dp(i-1, c), dp(i, c - i*i) + 1) # i是无穷个的，所以取了不会i-1 但是不取就是i-1
# class Solution:
#     def numSquares(self, n: int) -> int:

#         return dp(isqrt(n), n)
