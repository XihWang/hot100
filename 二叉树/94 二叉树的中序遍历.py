# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O（n） 空间O（h）
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            res.append(root.val)
            traverse(root.right)
        traverse(root)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 用递归和迭代的方式都使用了辅助的空间，而莫里斯遍历的优点是没有使用任何辅助空间。缺点是改变了整个树的结构，强行把一棵二叉树改成一段链表结构。
# 找到root的左节点的最右孩子，把root及其右边挂到这个最右孩子后面 最后变成一个链表
# class Solution(object):
# 	def inorderTraversal(self, root):
# 		"""
# 		:type root: TreeNode
# 		:rtype: List[int]
# 		"""
# 		res = []
# 		pre = None
# 		while root:
# 			# 如果左节点不为空，就将当前节点连带右子树全部挂到
# 			# 左节点的最右子树下面
# 			if root.left:
# 				pre = root.left
# 				while pre.right:
# 					pre = pre.right
# 				pre.right = root
# 				# 将root指向root的left
# 				tmp = root
# 				root = root.left
# 				tmp.left = None
# 			# 左子树为空，则打印这个节点，并向右边遍历
# 			else:
# 				res.append(root.val)
# 				root = root.right
# 		return res


# 作者：王尼玛
# 链接：https://leetcode.cn/problems/binary-tree-inorder-traversal/solutions/96765/dong-hua-yan-shi-94-er-cha-shu-de-zhong-xu-bian-li/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 用堆栈模拟递归
# class Solution(object):
# 	def inorderTraversal(self, root):
# 		"""
# 		:type root: TreeNode
# 		:rtype: List[int]
# 		"""
# 		res = []
# 		stack = []
# 		while stack or root:
# 			# 不断往左子树方向走，每走一次就将当前节点保存到栈中
# 			# 这是模拟递归的调用
# 			while root: # if root也可以
# 				stack.append(root)
# 				root = root.left
# 			# 当前节点为空，说明左边走到头了，从栈中弹出节点并保存
# 			# 然后转向右边节点，继续上面整个过程
# 			else:
# 				tmp = stack.pop()
# 				res.append(tmp.val)
# 				root = tmp.right
# 		return res

# 作者：王尼玛
# 链接：https://leetcode.cn/problems/binary-tree-inorder-traversal/solutions/96765/dong-hua-yan-shi-94-er-cha-shu-de-zhong-xu-bian-li/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。