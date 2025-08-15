class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        fresh = 0
        q = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        while q and fresh:
            qlen = len(q)
            res += 1
            # 同一个阶段的橘子都腐烂一次才扩散
            for i in range(qlen):
                x, y = q.pop(0)
                for dirx, diry in direction:
                    nextx, nexty = x + dirx, y + diry
                    if 0 <= nextx <= m-1 and 0 <= nexty <= n-1 and grid[nextx][nexty] == 1:
                        grid[nextx][nexty] = 2
                        q.append((nextx, nexty))
                        fresh -= 1

        return -1 if fresh else res