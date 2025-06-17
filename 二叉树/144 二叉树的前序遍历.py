# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # 通过迭代完成任务
    def __init__(self):
        self.res = []
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        self.traverse(root)
        return self.res

    def traverse(self, root):
        if root == None:
            return
        self.res.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)

    # 定义：输入一棵二叉树的根节点，返回这棵树的前序遍历结果
    # 通过分解完成任务 但是时间复杂度会高
    # def preorderTraversal(self, root):
    #     res = []
    #     if root == None:
    #         return res
    #     # 前序遍历的结果，root.val 在第一个
    #     res.append(root.val)
    #     # 利用函数定义，后面接着左子树的前序遍历结果
    #     res.extend(self.preorderTraversal(root.left))
    #     # 利用函数定义，最后接着右子树的前序遍历结果
    #     res.extend(self.preorderTraversal(root.right))
    #     return res