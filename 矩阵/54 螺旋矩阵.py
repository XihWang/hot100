from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = j = di = 0
        res = []
        for _ in range(m * n):
            res.append(matrix[i][j])
            matrix[i][j] = None
            x, y = i + DIRS[di][0], j + DIRS[di][1]
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] == None:
                di = (di + 1) % 4
            i, j = i + DIRS[di][0], j + DIRS[di][1]
        return res


