from collections import deque


class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        neighbor = [[3, 1], [0, 4, 2], [1, 5], [0, 4], [3, 1, 5], [4, 2]]
        boardls = []
        for i in board:
            boardls.extend(i)
        q = deque()
        visit = []
        q.append(boardls)
        visit.append(boardls)
        step = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.popleft()
                if cur == [1,2,3,4,5,0]:
                    return step
                output = []
                for i in neighbor[cur.index(0)]:
                    tmp = cur[:]  # 注意浅拷贝的问题
                    tmp[i], tmp[cur.index(0)] = cur[cur.index(0)], cur[i]
                    output.append(tmp)
                for i in output:
                    if i not in visit:
                        visit.append(i)
                        q.append(i)
            step += 1
        return -1


