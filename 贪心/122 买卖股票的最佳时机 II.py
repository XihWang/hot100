# from typing import List
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         ls = [0] * (len(prices) + 1)
#         res = 0
#         for i in range(1, len(prices)):
#             ls[i] = prices[i] - prices[i - 1]
#             if ls[i] > 0:
#                 res = res + ls[i]
#         return res


from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] - prices[i] > 0:
                res = res + prices[i + 1] - prices[i]
        return res
