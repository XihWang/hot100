# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#
#     def isSymmetric(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: bool
#         """
#         pre = root
#         self.invert(root)
#         return root == pre
#     def invert(self, root):
#         if root == None:
#             return True
#         self.invert(root.left)
#         self.invert(root.right)
#         root.right, root.left = root.left, root.right


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.isSameTree(root.left, root.right)

    def isSameTree(self, p, q):
        if p is None or q is None:
            return p is q
        return p.val == q.val and self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if p is None or q is None:
                return p is q
            return p.val == q.val and isSameTree(p.left, q.right) and isSameTree(p.right, q.left)

        return isSameTree(root.left, root.right)








