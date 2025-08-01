# bfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(q):
            while q:
                # qlen = len(q)
                # for i in range(qlen):
                x, y = q.pop(0)
                for dirx, diry in direction:
                    nextx = x + dirx
                    nexty = y + diry
                    if 0 <= nextx <= m - 1 and 0 <= nexty <= n - 1 and grid[nextx][nexty] == '1':
                        grid[nextx][nexty] = '0'
                        q.append((nextx, nexty))

        res = 0
        m = len(grid)
        n = len(grid[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    q = [(i, j)]
                    grid[i][j] == '0'  # 有没有这行都是对的 因为都循环下去了 这个是0还是1就无所谓了 建议有0吧 这样符合逻辑
                    bfs(q)
        return res

# dfs
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         def dfs(i, j):
#             for dirx, diry in direction:
#                 nextx, nexty = i + dirx, j + diry
#                 if 0 <= nextx <= m - 1 and 0 <= nexty <= n - 1 and grid[nextx][nexty] == '1':
#                 # 终止条件蕴含在这个条件判断中了
#                     grid[nextx][nexty] = '0'
#                     dfs(nextx, nexty)

#         res = 0
#         direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#         m = len(grid)
#         n = len(grid[0])
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     grid[i][j] = '0'
#                     dfs(i, j)
#                     res += 1
#         return res               