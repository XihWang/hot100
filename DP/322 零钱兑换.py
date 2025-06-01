class Solution(object):
    def coinChange(self, coins, amount):
        n = len(coins)
        @cache
        def dp(i, c):
            if i < 0: # 这里边界0也要进行考虑 所以是<0 注意这里和279的不同之处
                return 0 if c == 0 else inf
            if coins[i] > c:
                return dp(i - 1, c)
            return min(dp(i-1,c), dp(i, c - coins[i]) + 1)
        res = dp(n-1, amount)
        return res if res < inf else -1

# 时间爆了
# class Solution(object):
#     def coinChange(self, coins, amount):
#         n = len(coins)
#         memo = [[inf]*(amount+1) for _ in range(n)]
#         def dp(i, c):
#             if i < 0:
#                 return 0 if c == 0 else inf
#             if memo[i][c] != inf:
#                 return memo[i][c]
#             if coins[i] > c:
#                 return dp(i - 1, c)
#             memo[i][c] = min(dp(i-1,c), dp(i, c - coins[i]) + 1)
#             return memo[i][c]
#         res = dp(n-1, amount)
#         return res if res < inf else -1