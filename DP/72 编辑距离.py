# 没有备忘录的暴力解法 时间会溢出

# class Solution(object):
#     def minDistance(self, word1, word2):
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: int
#         """
#         def dp(i, j):
#             if i == -1:
#                 return j + 1
#             if j == -1:
#                 return i + 1
#             if word1[i] == word2[j]:
#                 return dp(i-1, j-1)
#             else:
#                 return min(
#                     dp(i-1, j) + 1, # 删除
#                     dp(i, j-1) + 1, # 插入
#                     dp(i-1, j-1) + 1 # 替换
#                 )
#         return dp(len(word1)-1, len(word2)-1)



class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        memo = [[float('inf')] * (len(word2)+1) for i in range(len(word1)+1)]
        def dp(i, j):
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1
            if memo[i][j] != float('inf'):
                return memo[i][j]
            if word1[i] == word2[j]:
                memo[i][j] = dp(i-1, j-1)
            else:
                memo[i][j] = min(
                    dp(i-1, j) + 1, # 删除
                    dp(i, j-1) + 1, # 插入
                    dp(i-1, j-1) + 1 # 替换
                )
            return memo[i][j]
        return dp(len(word1)-1, len(word2)-1)