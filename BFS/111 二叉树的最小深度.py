# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        q = deque()
        q.append(root)
        res = 0
        if root == None:
            return 0
        while q:
            sz = len(q)
            for i in range(sz):
                node = q.popleft()
                if node.left == None and node.right == None:
                    res += 1
                    return res
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            res += 1
        return res


