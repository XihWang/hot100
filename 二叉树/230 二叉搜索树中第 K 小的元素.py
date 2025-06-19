# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        midarr = []
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            midarr.append(root.val)
            traverse(root.right)
        traverse(root)
        return midarr[k - 1]