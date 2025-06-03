# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         n = len(text1)
#         m = len(text2)
#         @cache # 其他语言用二维数组
#         def dp(i,j): #text1前i个字符和text2前j个字符的公共子序列长度是多少
#             if i < 0 or j < 0:
#                 return 0
#             if text1[i] == text2[j]:
#                 return dp(i-1, j-1) + 1
#             else:
#                 return max(dp(i-1, j), dp(i, j - 1))
#         return dp(n-1, m-1)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        f = [[0] * (m+1) for _ in range(n + 1)]
        for i,x in enumerate(text1):
            for j,y in enumerate(text2):
                if x == y:
                    f[i+1][j+1] = f[i][j] + 1
                else:
                    f[i+1][j+1] = max(f[i][j+1], f[i+1][j])  # 注意让索引没有减号 减了多少就反应在f初始化的加多少，比如这里-1都变成了+0 都变大了1，所以初始化的时候n和m都要多1
        return f[n][m]
