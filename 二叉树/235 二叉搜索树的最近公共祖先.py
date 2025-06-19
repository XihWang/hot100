# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        x = root.val
        if q.val < x and p.val < x:
            return self.lowestCommonAncestor(root.left, p, q)
        if q.val > x and p.val > x:
            return self.lowestCommonAncestor(root.right, p, q)
        return root  # 一个在左一个在右边那么当年节点就是祖先/当年节点是q或者p，那么当前节点就是祖先