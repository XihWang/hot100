from collections import deque


class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadends = set(deadends)
        start = '0000'
        q = deque()
        q.append(start)
        step = 0
        visit = set()
        visit.add('0000')

        def up(string, i):
            ls = list(string)
            if ls[i] == '9':
                ls[i] = '0'
            else:
                ls[i] = chr(ord(ls[i]) + 1)
            return ''.join(ls)

        def down(string, i):
            ls = list(string)
            if ls[i] == '0':
                ls[i] = '9'
            else:
                ls[i] = chr(ord(ls[i]) - 1)
            return ''.join(ls)

        while q:
            sz = len(q)
            for i in range(sz):
                cur = q.popleft()
                if cur == target:
                    return step
                # visit.add(cur)
                neighbors = []
                for j in range(4):
                    upstr = up(cur, j)
                    downstr = down(cur, j)
                    neighbors.append(upstr)
                    neighbors.append(downstr)
                for neighbor in neighbors:
                    if neighbor not in deadends and neighbor not in visit:
                        q.append(neighbor)
                        visit.add(neighbor)


            step += 1
        return -1





