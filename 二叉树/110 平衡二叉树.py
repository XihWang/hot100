# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxdepth(root):
            if not root:
                return 0
            leftmax = maxdepth(root.left)
            if leftmax == -1:
                return -1
            rightmax = maxdepth(root.right)
            if rightmax == -1 or abs(rightmax - leftmax) > 1:
                return -1
            return 1 + max(leftmax, rightmax)

        return maxdepth(root) != -1

