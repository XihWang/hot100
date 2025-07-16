# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        p = q = head
        ls = []
        while p:
            ls.append(p.val)
            p = p.next
        ls.sort()

        for i in ls:
            q.val = i
            q = q.next
        return head