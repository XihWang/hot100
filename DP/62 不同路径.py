class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 到（i,j）的路径数目
        path = [[1] * (n+1) for i in range(m+1)]
        for i in range(1, m):
            for j in range(1, n):
                path[i+1][j+1] = path[i+1][j] +path[i][j+1]
        return path[m][n]

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         @cache  # 缓存装饰器，避免重复计算 dfs 的结果（一行代码实现记忆化）
#         def dfs(i: int, j: int) -> int:
#             if i < 0 or j < 0:
#                 return 0
#             if i == 0 and j == 0:
#                 return 1
#             return dfs(i - 1, j) + dfs(i, j - 1)
#         return dfs(m - 1, n - 1)


# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         return comb(m + n - 2, m - 1)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/unique-paths/solutions/3062432/liang-chong-fang-fa-dong-tai-gui-hua-zu-o5k32/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。