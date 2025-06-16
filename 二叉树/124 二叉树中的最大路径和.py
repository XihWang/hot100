# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf
        def dfs(root):
            if root is None:
                return 0
            l_val = dfs(root.left)
            r_val = dfs(root.right)
            nonlocal ans
            ans = max(ans, l_val + r_val + root.val)
            return max(max(l_val, r_val) + root.val, 0)
        dfs(root)
        return ans