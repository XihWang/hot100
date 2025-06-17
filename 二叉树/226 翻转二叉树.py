# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 方法一 遍历
# class Solution(object):
#     def invertTree(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: Optional[TreeNode]
#         """
#         self.invert(root)
#         return root
#
#     def invert(self, root):
#         if root == None:
#             return
#         root.left, root.right = root.right, root.left
#         self.invert(root.left)
#         self.invert(root.right)


# 方法二 分解
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root == None:
            return
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root
