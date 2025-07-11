# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        p = head
        dummy = ListNode(-1)
        dummy.next = head
        q = dummy
        # cur = head.next if head else None
        while p and p.next:
            tmp = p.next
            p.next = p.next.next
            tmp.next = p
            q.next = tmp
            q = p
            p = p.next

        # if cur is None:
        #     return head
        # else:
        #     return cur
        return dummy.next