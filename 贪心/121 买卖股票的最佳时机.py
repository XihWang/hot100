
# 这个方法和下面的方法一样的 但是时间会长很多 因为min每次都对前面所有数据求最小值 这样时间最后会溢出的
# from typing import List
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         res = 0
#         for i in range(1, len(prices)):
#             profit = prices[i] - min(prices[:i])
#             res = max (res, profit)
#         return res

# 当前值减前面值的最小值的列表的max
# from typing import List
#
#
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         res = 0
#         minprice = prices[0]
#         for i in range(1, len(prices)):
#             profit = prices[i] - minprice
#             res = max(res, profit)
#             minprice = min(prices[i], minprice)
#         return res

# 动态规划
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0是持有这只股票的手上现金  1是不持有这只股票的手上现金
        n = len(prices)
        dp = [[0] * 2 for i in range(n)]
        dp[0][0] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], -prices[i])
            dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0])
        return dp[n - 1][1]

# 差分数组 + 前缀和
# from typing import List
#
#
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         # 0是持有这只股票的手上现金  1是不持有这只股票的手上现金
#         n = len(prices)
#         sub = []
#         for i in range(1, n):
#             sub.append(prices[i] - prices[i - 1])
#         # 相当于当天买入第二天卖出 能赚多少钱
#         # sub的前缀和就相当于前面几天能赚多少钱
#         presum = []
#         total = 0
#         for i in sub:
#             total += i
#             presum.append(total)
#         # 之后在53的方法 求最大子数组的和
#         # 花里胡哨
#         # 不如方法一
#         # todo(后续用53的方法)

