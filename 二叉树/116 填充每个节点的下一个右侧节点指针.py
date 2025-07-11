"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return
        self.conn(root.left, root.right)
        return root

    def conn(self, left, right):
        if left is None or right is None:
            return
        left.next = right
        self.conn(left.left, left.right)
        self.conn(left.right, right.left)
        self.conn(right.left, right.right)

