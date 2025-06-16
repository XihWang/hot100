# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def flatten(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: None Do not return anything, modify root in-place instead.
#         """
#         self.circle(root)
#         return root
#
#     def circle(self,root):
#         if root == None:
#             return
#         root.left, root.right = root.right, root.left
#         p = root
#         while p.right:
#             p = p.right
#         p.right = root.left
#         self.circle(root.left)
#         self.circle(root.right)


class Solution:
    # 定义：将以 root 为根的树拉平为链表
    def flatten(self, root):
        # base case
        if root is None:
            return

        # 利用定义，把左右子树拉平
        self.flatten(root.left)
        self.flatten(root.right)

        # 后序遍历位置
        # 1、左右子树已经被拉平成一条链表
        left = root.left
        right = root.right

        # 2、将左子树作为右子树
        root.left = None
        root.right = left

        # 3、将原先的右子树接到当前右子树的末端
        p = root
        while p.right is not None:
            p = p.right
        p.right = right
