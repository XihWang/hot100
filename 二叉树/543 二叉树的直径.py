# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.depth = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxdepth(root)
        return self.depth

    def maxdepth(self, root):
        if root == None:
            return 0
        leftmax = self.maxdepth(root.left)
        rightmax = self.maxdepth(root.right)
        mydepth = leftmax + rightmax
        self.depth = max(self.depth, mydepth)
        return max(leftmax, rightmax) + 1