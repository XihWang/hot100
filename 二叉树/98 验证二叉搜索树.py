# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], left = -inf, right = inf) -> bool:
        if not root:
            return True
        x = root.val
        return left < x < right and self.isValidBST(root.left, left, x) and self.isValidBST(root.right, x, right)


# class Solution:
#     pre = -inf
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True
#         if not self.isValidBST(root.left) or root.val <= self.pre:
#             return False
#         self.pre = root.val
#         return self.isValidBST(root.right)

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         def dfs(node: Optional[TreeNode]) -> Tuple:
#             if node is None:
#                 return inf, -inf
#             l_min, l_max = dfs(node.left)
#             r_min, r_max = dfs(node.right)
#             x = node.val
#             # 也可以在递归完左子树之后立刻判断，如果发现不是二叉搜索树，就不用递归右子树了
#             if x <= l_max or x >= r_min:
#                 return -inf, inf
#             return min(l_min, x), max(r_max, x)
#         return dfs(root)[1] != inf

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/validate-binary-search-tree/solutions/2020306/qian-xu-zhong-xu-hou-xu-san-chong-fang-f-yxvh/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
