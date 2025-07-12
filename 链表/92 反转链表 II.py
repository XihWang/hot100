# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        p = dummy
        for i in range(left + 1):
            p = p.next
        pre = None
        cur = p
        for i in range(right - left + 1):
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        p.next.next = cur
        p.next = pre
        return dummy.next
