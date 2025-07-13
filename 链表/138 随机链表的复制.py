#
# # Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random
#
#
# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         p = head
#         dummy = Node(-1)
#         qzone = dummy
#         node_map = {}
#         while p:
#             new_node = Node(p.val)
#             node_map[p] = new_node
#             qzone.next = new_node
#             qzone = qzone.next
#             p = p.next
#         p = head
#         qzone = dummy.next
#         while p:
#             if p.random:
#                 qzone.random = node_map[p.random]
#             p = p.next
#             qzone = qzone.next
#         return dummy.next


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        if head is None:
            return
        while cur:
            cur.next = Node(cur.val, cur.next)
            cur = cur.next.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        cur = head.next

        # 这里前面都是中间分开的处理 所以nextnext是只要while cur就可以了
        # 但是这里是删除的操作 需要while cur.next
        while cur.next:
            cur.next = cur.next.next
            cur = cur.next

        return head.next




