# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            vals = []
            for _ in range(len(queue)):
                outq = queue.pop(0)
                vals.append(outq.val)
                if outq.left:
                    queue.append(outq.left)
                if outq.right:
                    queue.append(outq.right)
            res.append(vals)
        return res


