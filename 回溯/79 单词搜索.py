class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])
        cnt = Counter(c for row in board for c in row)
        if not cnt >= Counter(word):  # 每个元素要严格大于等于对应的元素，对于没有的元素，认定它的数量为0
            return False
        if cnt[word[-1]] < cnt[word[0]]:
            word = word[::-1]

        def dfs(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            board[i][j] = ''  # 标记访问过 防止走回头路
            for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= x < m and 0 <= y < n and dfs(x, y, k + 1):
                    return True
            # ij点位四个方向都没有 就恢复现场 返回false
            board[i][j] = word[k]
            return False

        return any(dfs(i, j, 0) for i in range(m) for j in range(n))
